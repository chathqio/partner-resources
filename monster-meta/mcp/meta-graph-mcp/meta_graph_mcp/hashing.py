"""SHA256 PII normalization for Custom Audience `users` and CAPI `user_data`.

Per rebuild/SCHEMA-VERIFICATION.md §2 (verified v25.0). Raw PII never leaves
this process: hashing happens here, before anything is sent. Identifiers that
must stay raw (EXTERN_ID / MADID / external_id / client_ip / UA / fbc / fbp /
LOOKALIKE_VALUE) are passed through unhashed by design.

SHA256 output = lowercase hex.
"""

import hashlib
import re

_NON_DIGIT = re.compile(r"\D")
_PUNCT_WS = re.compile(r"[^a-z0-9]")


def _sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _norm_email(v: str) -> str:
    return v.strip().lower()


def _norm_phone(v: str, country: str = "") -> str:
    d = _NON_DIGIT.sub("", str(v)).lstrip("0")
    return d


def _norm_name(v: str) -> str:
    # lowercase, drop punctuation/whitespace; keep unicode letters (FN/LN may
    # carry non-Roman per spec, so only strip ASCII punctuation/space).
    return re.sub(r"[\s\W]+", "", v.strip().lower(), flags=re.UNICODE)


def _norm_zip(v: str) -> str:
    z = v.strip().lower().replace(" ", "")
    # US: first 5 digits if it looks US-numeric.
    if z[:5].isdigit():
        return z[:5]
    return z


# Custom Audience `users` schema keys -> (hash?, normalizer)
_CA_RULES = {
    "EMAIL": (True, _norm_email),
    "PHONE": (True, _norm_phone),
    "GEN": (True, lambda v: v.strip().lower()[:1]),
    "DOBY": (True, lambda v: re.sub(r"\D", "", v)[:4]),
    "DOBM": (True, lambda v: re.sub(r"\D", "", v).zfill(2)[:2]),
    "DOBD": (True, lambda v: re.sub(r"\D", "", v).zfill(2)[:2]),
    "FN": (True, _norm_name),
    "LN": (True, _norm_name),
    "FI": (True, lambda v: v.strip().lower()[:1]),
    "ST": (True, lambda v: _PUNCT_WS.sub("", v.strip().lower())),
    "CT": (True, lambda v: _PUNCT_WS.sub("", v.strip().lower())),
    "ZIP": (True, _norm_zip),
    "COUNTRY": (True, lambda v: v.strip().lower()[:2]),
    "MADID": (False, lambda v: v.strip().lower()),  # raw, keep hyphens
    "EXTERN_ID": (False, lambda v: str(v)),  # raw
    "LOOKALIKE_VALUE": (False, lambda v: v),  # numeric weight, not a key
}


def hash_ca_users(schema, data: list) -> list:
    """Normalize+hash a Custom Audience `users` payload `data`.

    schema: a single key string (e.g. 'EMAIL') or a list of keys (multi-key).
    data:   list of scalars (single-key) or list of row-lists (multi-key),
            aligned to `schema`. Already-hashed 64-hex values are passed through.
    Returns the transformed `data` ready for the /users edge.
    """
    keys = [schema] if isinstance(schema, str) else list(schema)

    def conv(key: str, val):
        if val is None:
            return val
        rule = _CA_RULES.get(str(key).upper())
        if not rule:
            return val  # unknown key -> don't gate, send as-is
        do_hash, norm = rule
        s = str(val)
        if do_hash and re.fullmatch(r"[0-9a-f]{64}", s):
            return s  # already hashed
        n = norm(s)
        return _sha(n) if do_hash else n

    out = []
    for row in data:
        if isinstance(row, (list, tuple)):
            out.append([conv(keys[i], v) for i, v in enumerate(row)])
        else:
            out.append(conv(keys[0], row))
    return out


# CAPI user_data: hashed PII keys vs raw identifier keys.
_CAPI_HASH = {
    "em": _norm_email,
    "ph": _norm_phone,
    "fn": _norm_name,
    "ln": _norm_name,
    "ge": lambda v: v.strip().lower()[:1],
    "db": lambda v: re.sub(r"\D", "", v)[:8],
    "ct": lambda v: _PUNCT_WS.sub("", v.strip().lower()),
    "st": lambda v: _PUNCT_WS.sub("", v.strip().lower()),
    "zp": _norm_zip,
    "country": lambda v: v.strip().lower()[:2],
}
_CAPI_RAW = {
    "external_id", "client_ip_address", "client_user_agent", "fbc", "fbp",
    "subscription_id", "fb_login_id", "lead_id", "anon_id", "madid", "fbclid",
}


def hash_capi_user_data(user_data: dict) -> dict:
    """Normalize+hash a CAPI server-event `user_data` object in place-safe copy.
    Hashed keys may be scalars or lists; raw keys pass through untouched.
    Unknown keys pass through (never gate)."""
    out: dict = {}
    for k, v in (user_data or {}).items():
        if k in _CAPI_RAW or k not in _CAPI_HASH:
            out[k] = v
            continue
        norm = _CAPI_HASH[k]

        def one(x):
            s = str(x)
            if re.fullmatch(r"[0-9a-f]{64}", s):
                return s
            return _sha(norm(s))

        out[k] = [one(x) for x in v] if isinstance(v, (list, tuple)) else one(v)
    return out

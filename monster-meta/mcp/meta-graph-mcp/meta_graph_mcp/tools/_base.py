"""Shared helpers for named convenience tools.

THE NON-GATING CONTRACT (every named tool MUST obey):
  1. A named tool builds an endpoint + sensible defaults, then routes through
     client.request — the same single path the primitives use.
  2. It NEVER rejects an input the Graph API would accept. No allow-lists, no
     "invalid objective" / "unsupported field" raises. Validation that helps is
     a `warning` in the response, never a refusal, and is always overridable.
  3. Every tool takes `extra: dict | None` (read tools) / writes also take
     `extra` — merged into params/body LAST and forwarded untouched, so any
     field this wrapper didn't model is still reachable without dropping to
     graph_*. `fields` is always overridable on reads.
  4. Default field lists are GENEROUS (we surface fields; we don't hide them
     like the third-party did). Callers can always override `fields`.
  5. Writes expose `dry_run` (local preview) and `validate_only` (Meta-side
     validate via execution_options) — previews/conventions, never gates.
"""

import json

from ..client import request as _request
from ..redact import redact


def dump(obj) -> str:
    return json.dumps(redact(obj), indent=2, default=str)


def merge(base: dict | None, extra: dict | None) -> dict:
    """extra is the open passthrough — it wins, and may add anything."""
    out = dict(base or {})
    if extra:
        out.update(extra)
    return out


def with_validate_only(body: dict, validate_only: bool) -> dict:
    if not validate_only:
        return body
    eo = list(body.get("execution_options") or [])
    if "validate_only" not in eo:
        eo.append("validate_only")
    return {**body, "execution_options": eo}


def get(
    path: str,
    default_fields: str,
    *,
    fields: str = "",
    params: dict | None = None,
    limit: int | None = None,
    extra: dict | None = None,
    version: str | None = None,
) -> str:
    """Generic non-gating READ. `fields` overrides default_fields; `extra`
    merges last (open passthrough); nothing is filtered out."""
    p: dict = {"fields": fields or default_fields}
    if limit is not None:
        p["limit"] = limit
    p = merge(p, params)
    p = merge(p, extra)
    return dump(_request("GET", path, params=p, version=version))


def write(
    path: str,
    body: dict,
    *,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
    version: str | None = None,
) -> str:
    """Generic non-gating WRITE (Graph POST = create or update). `extra` merges
    last; `dry_run` previews locally; `validate_only` asks Meta to validate
    without applying. Never rejects a field the API would accept."""
    b = merge(body, extra)
    b = with_validate_only(b, validate_only)
    return dump(_request("POST", path, body=b, version=version, dry_run=dry_run))


def delete(
    path: str, *, dry_run: bool = False, version: str | None = None
) -> str:
    return dump(_request("DELETE", path, version=version, dry_run=dry_run))

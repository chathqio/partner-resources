"""The single execution path. Every tool in this server routes through here.

Guarantees that make "never refuse a valid Graph operation" structural:
- No field allow-lists. Whatever params/body a caller passes are sent as-is.
- Meta's error object is returned VERBATIM — an API rejection is never
  reinterpreted as a tool limitation.
- Any node/edge/field/edge and any API version is reachable.
"""

import hashlib
import hmac
import json
import os
import pathlib
import re
from urllib.parse import urlencode

import httpx

from .redact import redact, silence_http_logging

silence_http_logging()

DEFAULT_VERSION = os.environ.get("GRAPH_API_VERSION", "v25.0")
GRAPH_HOST = "https://graph.facebook.com"
# Optional. Empty by default so the server ships clean for the community —
# {account} only resolves when META_DEFAULT_ACCOUNT is explicitly set.
DEFAULT_ACCOUNT = os.environ.get("META_DEFAULT_ACCOUNT", "").strip()
READONLY = os.environ.get("META_GRAPH_READONLY", "0") == "1"
_APP_SECRET = os.environ.get("META_APP_SECRET", "").strip()


class TokenError(RuntimeError):
    """Raised when no access token can be resolved."""


def resolve_token() -> str:
    """env META_ACCESS_TOKEN -> env FB_TOKEN -> ~/.config/meta-ads-mcp/token_cache.json.

    The token value is never returned by any tool or written to any log.
    """
    tok = os.environ.get("META_ACCESS_TOKEN") or os.environ.get("FB_TOKEN")
    if tok:
        return tok.strip()
    cache = pathlib.Path.home() / ".config" / "meta-ads-mcp" / "token_cache.json"
    if cache.exists():
        try:
            data = json.loads(cache.read_text())
            tok = data.get("access_token") or data.get("token")
            if tok:
                return str(tok).strip()
        except (json.JSONDecodeError, OSError):
            pass
    raise TokenError(
        "No Meta token. Set META_ACCESS_TOKEN (rev-ops/.mcp.json -> "
        "mcpServers.meta-graph.env), or FB_TOKEN, or populate "
        "~/.config/meta-ads-mcp/token_cache.json."
    )


def _appsecret_proof(token: str) -> str | None:
    """appsecret_proof — required for some system-user tokens, recommended by
    Meta for all server-to-server calls. Active only if META_APP_SECRET is set."""
    if not _APP_SECRET:
        return None
    return hmac.new(
        _APP_SECRET.encode("utf-8"), token.encode("utf-8"), hashlib.sha256
    ).hexdigest()


def norm_path(path: str, version: str) -> str:
    """'act_1/campaigns', '123', 'me', a full URL, or '{account}' -> absolute URL.

    Marketing API forbids unversioned calls, so a version is always injected
    for relative paths. Full URLs are passed through untouched.
    """
    path = path.strip()
    if "{account}" in path:
        if not DEFAULT_ACCOUNT:
            raise ValueError(
                "{account} used but META_DEFAULT_ACCOUNT is not set in the "
                "server env. Pass the explicit act_<id> instead."
            )
        path = path.replace("{account}", DEFAULT_ACCOUNT)
    if path.startswith("http://") or path.startswith("https://"):
        return path
    return f"{GRAPH_HOST}/{version}/{path.lstrip('/')}"


def encode_value(v):
    """Graph form-encoding: bool -> lowercased; dict/list -> compact JSON."""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (dict, list)):
        return json.dumps(v, separators=(",", ":"))
    return str(v)


def _maybe_json(raw: str):
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return raw


def _rate_limit(headers) -> dict:
    """Surface Meta's throttling headers instead of hiding them."""
    out = {}
    for h in ("x-app-usage", "x-business-use-case-usage", "x-ad-account-usage"):
        if h in headers:
            out[h] = _maybe_json(headers[h])
    return out


def request(
    method: str,
    path: str,
    *,
    params: dict | None = None,
    body: dict | None = None,
    version: str | None = None,
    dry_run: bool = False,
) -> dict:
    """Execute (or, with dry_run, preview) one Graph API call.

    Returns a structured envelope; Meta's error object is passed through verbatim.
    """
    version = version or DEFAULT_VERSION
    url = norm_path(path, version)
    method = method.upper()
    is_write = method in ("POST", "DELETE", "PUT")

    if dry_run:
        return {
            "dry_run": True,
            "method": method,
            "url": url,
            "params": {k: encode_value(v) for k, v in (params or {}).items()},
            "body": {k: encode_value(v) for k, v in (body or {}).items()}
            if body is not None
            else None,
        }
    if is_write and READONLY:
        return {
            "ok": False,
            "error": {"message": "META_GRAPH_READONLY=1 — writes disabled"},
        }

    token = resolve_token()
    q = {k: encode_value(v) for k, v in dict(params or {}).items()}
    q["access_token"] = token
    proof = _appsecret_proof(token)
    if proof:
        q["appsecret_proof"] = proof
    data = (
        {k: encode_value(v) for k, v in body.items()} if body is not None else None
    )

    try:
        with httpx.Client(timeout=60, follow_redirects=True) as client:
            resp = client.request(method, url, params=q, data=data)
        payload = _maybe_json(resp.text)
        env = {
            "ok": resp.is_success,
            "status": resp.status_code,
            "rate_limit": _rate_limit(resp.headers),
        }
        # Pass Meta's error through verbatim — never translate it into a
        # tool-level "unsupported".
        env["data" if resp.is_success else "error"] = payload
        return redact(env)
    except httpx.HTTPError as e:
        return {"ok": False, "status": None, "error": {"message": str(e)}}


def batch(
    requests_list: list,
    *,
    version: str | None = None,
    dry_run: bool = False,
) -> dict:
    """Graph Batch API — many ops in one round-trip.

    Each item: {method, path|relative_url, params?, body?}. relative_urls are
    version-prefixed automatically. Returns the array of sub-responses verbatim.
    """
    version = version or DEFAULT_VERSION
    # A leading "vNN" or "vNN.N" segment means the caller already versioned it.
    versioned = re.compile(r"^v\d+(\.\d+)?/")
    ops: list = []
    for r in requests_list:
        m = str(r.get("method", "GET")).upper()
        rel = str(r.get("relative_url") or r.get("path", "")).lstrip("/")
        if not rel.startswith("http") and not versioned.match(rel):
            rel = f"{version}/{rel}"
        prms = r.get("params")
        if prms and m == "GET":
            qs = urlencode({k: encode_value(v) for k, v in prms.items()})
            rel = f"{rel}?{qs}"
        op = {"method": m, "relative_url": rel}
        bdy = r.get("body")
        if bdy is not None and m in ("POST", "PUT", "DELETE"):
            op["body"] = urlencode({k: encode_value(v) for k, v in bdy.items()})
        ops.append(op)

    if dry_run:
        return {"dry_run": True, "method": "POST", "url": f"{GRAPH_HOST}/", "batch": ops}
    if READONLY and any(o["method"] in ("POST", "PUT", "DELETE") for o in ops):
        return {
            "ok": False,
            "error": {"message": "META_GRAPH_READONLY=1 — writes disabled"},
        }

    token = resolve_token()
    form = {"batch": json.dumps(ops), "access_token": token}
    proof = _appsecret_proof(token)
    if proof:
        form["appsecret_proof"] = proof
    try:
        with httpx.Client(timeout=120, follow_redirects=True) as client:
            resp = client.post(f"{GRAPH_HOST}/", data=form)
        payload = _maybe_json(resp.text)
        env = {
            "ok": resp.is_success,
            "status": resp.status_code,
            "rate_limit": _rate_limit(resp.headers),
        }
        env["data" if resp.is_success else "error"] = payload
        return redact(env)
    except httpx.HTTPError as e:
        return {"ok": False, "status": None, "error": {"message": str(e)}}


def auto_paginate(
    path: str,
    *,
    params: dict | None = None,
    limit: int = 50,
    max_pages: int = 5,
    version: str | None = None,
) -> dict:
    """GET an edge and auto-follow paging.cursors.after up to max_pages."""
    p = dict(params or {})
    p["limit"] = limit
    out: list = []
    pages = 0
    after = None
    while pages < max_pages:
        if after:
            p["after"] = after
        res = request("GET", path, params=p, version=version)
        if not res.get("ok"):
            return redact(res)
        body = res["data"]
        if isinstance(body, dict):
            out.extend(body.get("data", []))
            after = (body.get("paging", {}).get("cursors", {}) or {}).get("after")
        else:
            after = None
        pages += 1
        if not after:
            break
    return redact(
        {"ok": True, "pages_fetched": pages, "count": len(out), "data": out}
    )

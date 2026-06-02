"""Generic Graph API passthrough — the structural guarantee that this server
never refuses an operation the Graph API supports.

If a named tool elsewhere doesn't model something, these always can: any node,
any edge, any field, any HTTP verb, any API version.
"""

import json

from .. import __version__
from ..client import (
    DEFAULT_ACCOUNT,
    DEFAULT_VERSION,
    GRAPH_HOST,
    auto_paginate,
)
from ..client import batch as _batch
from ..client import request as _request
from ..client import resolve_token
from ..redact import redact


def _dump(obj) -> str:
    return json.dumps(redact(obj), indent=2, default=str)


def graph_get(
    path: str,
    fields: str = "",
    params: dict | None = None,
    limit: int | None = None,
    version: str | None = None,
) -> str:
    """GET any Graph API node or edge.

    path: node/edge — e.g. '120245082687230783', 'act_123/campaigns', 'me',
          a full URL, or '{account}' for META_DEFAULT_ACCOUNT.
    fields: comma-separated field list (supports nested expansion, e.g.
            'id,name,adsets{name,daily_budget,ads{name}}').
    params: any extra query params, e.g. {'effective_status':['ACTIVE'],
            'time_range':{'since':'2026-01-01','until':'2026-01-31'}}.
    version: override the API version for this call (default v25.0).
    """
    p = dict(params or {})
    if fields:
        p["fields"] = fields
    if limit is not None:
        p["limit"] = limit
    return _dump(_request("GET", path, params=p, version=version))


def graph_post(
    path: str,
    data: dict,
    dry_run: bool = False,
    validate_only: bool = False,
    version: str | None = None,
) -> str:
    """POST to any node/edge — Graph uses POST for BOTH create and update.

    data: full field set. Nested dict/list values (promoted_object,
          tracking_specs, targeting, asset_feed_spec, ...) are auto JSON-encoded
          — pass them as real objects.
    validate_only: sends execution_options=['validate_only'] so Meta validates
                   the write WITHOUT applying it (true API-side dry run).
    dry_run: returns the exact request that WOULD be sent (no API call).

    Extendly convention: create/leave campaign objects PAUSED unless the user
    explicitly authorized activation. Budget changes are financially material —
    preview with dry_run/validate_only and confirm first. This is a convention,
    not a gate: any field the Graph API accepts is sent through unaltered.
    """
    body = dict(data or {})
    if validate_only:
        eo = body.get("execution_options")
        body["execution_options"] = list(eo or []) + (
            [] if eo and "validate_only" in eo else ["validate_only"]
        )
    return _dump(_request("POST", path, body=body, version=version, dry_run=dry_run))


def graph_delete(
    path: str, dry_run: bool = False, version: str | None = None
) -> str:
    """DELETE a Graph API node (ad, ad set, audience, ...).

    Prefer PAUSING over deleting campaign objects — deletion is irreversible and
    loses learning/history. dry_run previews without calling.
    """
    return _dump(_request("DELETE", path, version=version, dry_run=dry_run))


def graph_paginate(
    path: str,
    fields: str = "",
    params: dict | None = None,
    limit: int = 50,
    max_pages: int = 5,
    version: str | None = None,
) -> str:
    """GET an edge and auto-follow paging.cursors.after up to max_pages.
    Returns concatenated `data` plus a `pages_fetched` count."""
    p = dict(params or {})
    if fields:
        p["fields"] = fields
    return _dump(
        auto_paginate(
            path, params=p, limit=limit, max_pages=max_pages, version=version
        )
    )


def graph_batch(requests: list, dry_run: bool = False) -> str:
    """Graph Batch API — run many ops in one round-trip.

    requests: list of {method, path, params?, body?}. relative_urls are
              version-prefixed automatically. Example:
      [{"method":"GET","path":"{account}/campaigns","params":{"limit":2}},
       {"method":"POST","path":"<adset_id>","body":{"status":"PAUSED"}}]
    """
    return _dump(_batch(requests, dry_run=dry_run))


def graph_call(
    method: str,
    path: str,
    params: dict | None = None,
    body: dict | None = None,
    dry_run: bool = False,
    version: str | None = None,
) -> str:
    """Total escape hatch — any HTTP method, path, params, body, version.

    Use when no other tool fits. By construction this can perform anything the
    Graph API itself permits, so this server can never be the reason an
    operation 'isn't supported'.
    """
    return _dump(
        _request(
            method, path, params=params, body=body, version=version, dry_run=dry_run
        )
    )


def whoami() -> str:
    """Identify the active token: /me, granted scopes, expiry, validity.
    The token value itself is never returned. Run this first when debugging
    auth — before blaming a call."""
    me = _request("GET", "me", params={"fields": "id,name"})
    try:
        tok = resolve_token()
    except Exception as e:  # noqa: BLE001 — surface as data, don't crash the tool
        return _dump({"error": str(e)})
    dbg = _request(
        "GET", "debug_token", params={"input_token": tok, "access_token": tok}
    )
    info: dict = {}
    if dbg.get("ok") and isinstance(dbg.get("data"), dict):
        d = dbg["data"].get("data", {})
        info = {
            "app_id": d.get("app_id"),
            "type": d.get("type"),
            "scopes": d.get("scopes"),
            "expires_at": d.get("expires_at"),
            "data_access_expires_at": d.get("data_access_expires_at"),
            "is_valid": d.get("is_valid"),
        }
    return _dump(
        {
            "me": me.get("data"),
            "token": info,
            "default_account": DEFAULT_ACCOUNT or "(unset)",
            "graph_version": DEFAULT_VERSION,
            "server_version": __version__,
        }
    )


def meta_graph_help() -> str:
    """Quick reference: how this server is structured and common recipes."""
    return (
        f"meta-graph-mcp v{__version__} — Graph/Marketing API {DEFAULT_VERSION}\n"
        f"DEFAULT ACCOUNT: {DEFAULT_ACCOUNT or '(unset — pass act_<id> explicitly)'}\n\n"
        "PRINCIPLE: this server never refuses what the Graph API supports.\n"
        "If a named tool doesn't model a field, pass it anyway (named tools\n"
        "forward unknown params) or drop to the primitives below.\n\n"
        "PRIMITIVES:\n"
        "- graph_get(path, fields, params, limit, version)\n"
        "- graph_post(path, data, dry_run, validate_only, version)  # create OR update\n"
        "- graph_delete(path, dry_run, version)\n"
        "- graph_paginate(path, fields, params, limit, max_pages, version)\n"
        "- graph_batch(requests, dry_run)\n"
        "- graph_call(method, path, params, body, dry_run, version)  # escape hatch\n"
        "- whoami()\n\n"
        "RECIPES:\n"
        "- Campaigns: graph_get('{account}/campaigns',"
        " 'id,name,status,objective,daily_budget', {'effective_status':['ACTIVE']})\n"
        "- Ad set conversion config: graph_get('<adset_id>',"
        " 'name,promoted_object,optimization_goal,attribution_spec')\n"
        "- Repoint optimization pixel: graph_post('<adset_id>',"
        " {'promoted_object':{'pixel_id':'<id>','custom_event_type':'PURCHASE'}})\n"
        "- Rename an ad: graph_post('<ad_id>', {'name':'<new name>'})\n"
        "- Replace tracking_specs: graph_post('<ad_id>', {'tracking_specs':[...]})\n"
        "- Validate a write w/o applying: graph_post(id, {...}, validate_only=True)\n"
        "- Pause: graph_post('<id>', {'status':'PAUSED'})\n"
        "- Insights: graph_get('<id>/insights',"
        " 'spend,impressions,ctr,actions', {'date_preset':'last_7d'})\n"
        "Preview risky writes with dry_run=True or validate_only=True first.\n"
    )


_TOOLS = [
    graph_get,
    graph_post,
    graph_delete,
    graph_paginate,
    graph_batch,
    graph_call,
    whoami,
    meta_graph_help,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

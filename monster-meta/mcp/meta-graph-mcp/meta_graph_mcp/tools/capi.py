"""Conversions API tools — thin, non-gating wrappers (see _base.py contract).

Server-side events for pixels/datasets (`/{pixel_id}/events`) and offline
event sets (`/{offline_event_set_id}/events`). Same tool names as the
third-party meta-ads MCP so the skill rewrite is a pure prefix swap. PII in
`user_data` / `match_keys` is normalized + SHA256-hashed locally
(meta_graph_mcp.hashing) BEFORE any request leaves the process; no
`event_name` / `action_source` value is ever rejected.
"""

from . import _base
from .. import hashing


def _hash_events(events: list) -> list:
    """Normalize + hash the PII on each server event, leaving everything else
    (event_name, custom_data, raw identifiers, ...) untouched. `user_data` is
    the standard CAPI key; `match_keys` is the offline-events equivalent."""
    out = []
    for ev in events or []:
        e = dict(ev or {})
        if isinstance(e.get("user_data"), dict):
            e["user_data"] = hashing.hash_capi_user_data(e["user_data"])
        if isinstance(e.get("match_keys"), dict):
            e["match_keys"] = hashing.hash_capi_user_data(e["match_keys"])
        out.append(e)
    return out


def send_conversions(
    pixel_id: str,
    events: list,
    test_event_code: str = "",
    auto_hash: bool = True,
    partner_agent: str = "",
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Send Conversions API server events (`POST /{pixel_id}/events`).

    events: a list of server-event dicts (event_name, event_time,
            action_source, user_data, custom_data, ...). ANY event_name /
            action_source value is forwarded as-is — never rejected.
    auto_hash: True (default) → normalize + SHA256-hash each event's
               `user_data` locally before sending (raw PII never leaves this
               process). False → caller pre-hashed; pass through.
    test_event_code / partner_agent: added to the body only when given.
    extra: any additional body fields, forwarded untouched.
    """
    data = _hash_events(events) if auto_hash else list(events or [])
    body: dict = {"data": data}
    if test_event_code:
        body["test_event_code"] = test_event_code
    if partner_agent:
        body["partner_agent"] = partner_agent
    return _base.write(
        f"{pixel_id}/events", body, extra=extra, dry_run=dry_run
    )


def send_offline_conversions(
    offline_event_set_id: str,
    events: list,
    upload_tag: str = "",
    auto_hash: bool = True,
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Send offline conversion events
    (`POST /{offline_event_set_id}/events`).

    events: a list of offline-event dicts. ANY event_name value is forwarded
            as-is — never rejected.
    auto_hash: True (default) → normalize + SHA256-hash each event's
               `match_keys` / `user_data` locally before sending (raw PII
               never leaves this process). False → caller pre-hashed.
    upload_tag: added to the body only when given.
    extra: any additional body fields, forwarded untouched.
    """
    data = _hash_events(events) if auto_hash else list(events or [])
    body: dict = {"data": data}
    if upload_tag:
        body["upload_tag"] = upload_tag
    return _base.write(
        f"{offline_event_set_id}/events",
        body,
        extra=extra,
        dry_run=dry_run,
    )


_TOOLS = [
    send_conversions,
    send_offline_conversions,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

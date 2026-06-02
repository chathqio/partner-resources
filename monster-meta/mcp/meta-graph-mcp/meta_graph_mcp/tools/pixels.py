"""Pixel / dataset tools — thin, non-gating wrappers (see _base.py contract).

Same tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. Unlike the third-party: no field allow-list (generous defaults,
overridable via `fields`), every field reachable via `extra`, and sharing
routes through the single non-gating write path.

An AdsPixel id is also the dataset id used by the Conversions API.
"""

from .._account import acct
from . import _base

# Generous — surface the fields the third-party hid (code snippet, last fired
# time, ownership, data-use setting). Override via `fields`.
_PIXEL_FIELDS = (
    "id,name,code,last_fired_time,is_created_by_business,data_use_setting,"
    "creation_time,owner_ad_account,owner_business"
)


def get_pixels(
    account_id: str = "",
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """List ads pixels (datasets) for an ad account.

    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    """
    return _base.get(
        f"{acct(account_id)}/adspixels",
        _PIXEL_FIELDS,
        fields=fields,
        extra=extra,
    )


def get_pixel(
    pixel_id: str, fields: str = "", extra: dict | None = None
) -> str:
    """Full detail for one pixel/dataset (generous default fields; override via `fields`)."""
    return _base.get(pixel_id, _PIXEL_FIELDS, fields=fields, extra=extra)


def create_pixel(
    account_id: str = "",
    name: str = "",
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Create an ads pixel (dataset) on an ad account.

    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).
    name: the pixel name. Anything else (e.g. an explicit business id) goes
          through `extra`, merged last.
    dry_run: preview the request locally without calling Meta.
    """
    body: dict = {"name": name}
    return _base.write(
        f"{acct(account_id)}/adspixels",
        body,
        extra=extra,
        dry_run=dry_run,
    )


def get_pixel_stats(
    pixel_id: str,
    aggregation: str = "event",
    start_time: str = "",
    end_time: str = "",
    extra: dict | None = None,
) -> str:
    """Pixel firing stats.

    pixel_id: the AdsPixel/dataset id.
    aggregation: how to bucket the stats (default 'event'; e.g. 'device_type',
                 'browser_type', 'url', ...). Forwarded as-is — not validated.
    start_time/end_time: optional time bounds, forwarded if set.
    extra: any additional query params, forwarded untouched (merged last).
    """
    params: dict = {"aggregation": aggregation}
    if start_time:
        params["start_time"] = start_time
    if end_time:
        params["end_time"] = end_time
    return _base.get(
        f"{pixel_id}/stats",
        "",
        params=params,
        extra=extra,
    )


def share_pixel(
    pixel_id: str,
    account_ids: list | None = None,
    business_ids: list | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Share a pixel with other ad accounts and/or businesses.

    account_ids: ad accounts to grant access -> POST {pixel_id}/shared_accounts.
    business_ids: businesses (agencies) to grant access ->
                  POST {pixel_id}/shared_agencies.

    Both edges are separate Graph calls. To keep this a single non-gating write,
    when only one of the two is supplied that edge is called; when BOTH are
    supplied the shared_accounts call is made here — share the agencies in a
    second call (business_ids=[...] with no account_ids), or use graph_post on
    {pixel_id}/shared_agencies directly. account_ids/business_ids are forwarded
    as native lists (NOT serialized).
    dry_run: preview the request locally without calling Meta.
    """
    if account_ids is not None:
        return _base.write(
            f"{pixel_id}/shared_accounts",
            {"account_id": account_ids},
            extra=extra,
            dry_run=dry_run,
        )
    return _base.write(
        f"{pixel_id}/shared_agencies",
        {"business": business_ids if business_ids is not None else []},
        extra=extra,
        dry_run=dry_run,
    )


_TOOLS = [
    get_pixels,
    get_pixel,
    create_pixel,
    get_pixel_stats,
    share_pixel,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

"""Ad tools — thin, non-gating wrappers (see _base.py contract).

Same tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. Unlike the third-party: no fixed field allow-list, `update_ad`
allows `name` and *replaces* (not appends) `tracking_specs`, the `creative`
object is forwarded as a real object (not json.dumps'd), every field reachable
via `extra`.
"""

from .._account import acct
from . import _base

# Generous — surface fields the third-party hid (configured_status,
# effective_status, conversion_specs, source_ad_id, adlabels, ...). Override
# via `fields`.
_AD_FIELDS = (
    "id,name,adset_id,campaign_id,account_id,status,configured_status,"
    "effective_status,creative,tracking_specs,conversion_specs,"
    "conversion_domain,source_ad_id,adlabels,created_time,updated_time"
)


def get_ads(
    account_id: str = "",
    adset_id: str = "",
    campaign_id: str = "",
    limit: int = 25,
    fields: str = "",
    params: dict | None = None,
    extra: dict | None = None,
) -> str:
    """List ads, optionally scoped to an ad set or campaign.

    adset_id: list ads under one ad set (uses {adset_id}/ads).
    campaign_id: list ads under one campaign (uses {campaign_id}/ads).
    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT); used only when
                neither adset_id nor campaign_id is given.
    fields: override the (generous) default field list.
    params/extra: any additional query params, forwarded untouched.
    """
    if adset_id:
        path = f"{adset_id}/ads"
    elif campaign_id:
        path = f"{campaign_id}/ads"
    else:
        path = f"{acct(account_id)}/ads"
    return _base.get(
        path,
        _AD_FIELDS,
        fields=fields,
        params=params,
        limit=limit,
        extra=extra,
    )


def get_ad_details(
    ad_id: str, fields: str = "", extra: dict | None = None
) -> str:
    """Full detail for one ad (generous default fields; override via `fields`)."""
    return _base.get(ad_id, _AD_FIELDS, fields=fields, extra=extra)


def create_ad(
    account_id: str = "",
    name: str = "",
    adset_id: str = "",
    creative: dict | list | None = None,
    status: str = "PAUSED",
    tracking_specs: dict | list | None = None,
    conversion_domain: str | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Create an ad.

    creative: the creative spec, e.g. {"creative_id": "<id>"} or an inline
    object_story_spec — forwarded as a real object (the client encodes it; NOT
    json.dumps'd). tracking_specs is likewise passed through as an object.
    Convention: defaults to PAUSED. Anything not modeled here goes through
    `extra` and nothing is gated.
    """
    body: dict = {"name": name, "adset_id": adset_id, "status": status}
    if creative is not None:
        body["creative"] = creative
    if tracking_specs is not None:
        body["tracking_specs"] = tracking_specs
    if conversion_domain is not None:
        body["conversion_domain"] = conversion_domain
    return _base.write(
        f"{acct(account_id)}/ads",
        body,
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


def update_ad(
    ad_id: str,
    fields_to_update: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Update an ad. Pass any updatable field in `fields_to_update` (or
    `extra`) — name, status, creative, tracking_specs, conversion_domain,
    bid_amount, adlabels, ... Nothing is gated and there is no allow-list: this
    fixes the two third-party gaps directly — `name` is updatable here, and
    `tracking_specs` you pass *replaces* the existing specs (the third-party
    silently appended). Pass `creative`/`tracking_specs` as real objects (the
    client encodes them). Graph rejects what it won't accept and that error is
    returned verbatim. Status/creative swaps are material — preview with
    dry_run/validate_only first.
    """
    return _base.write(
        ad_id,
        dict(fields_to_update or {}),
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


def delete_ad(ad_id: str, dry_run: bool = False) -> str:
    """Delete an ad (prefer pausing — deletion loses learning/history)."""
    return _base.delete(ad_id, dry_run=dry_run)


_TOOLS = [
    get_ads,
    get_ad_details,
    create_ad,
    update_ad,
    delete_ad,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

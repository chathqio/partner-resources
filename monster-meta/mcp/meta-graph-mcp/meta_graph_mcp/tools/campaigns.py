"""Campaign tools — thin, non-gating wrappers (see _base.py contract).

Same tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. Unlike the third-party: no fixed field allow-list, no objective
rejection, every field reachable via `extra`.
"""

from .._account import acct
from . import _base

# Generous — surface fields the third-party hid (effective_status,
# promoted_object, budget_remaining, bid_strategy, ...). Override via `fields`.
_CAMPAIGN_FIELDS = (
    "id,name,objective,status,configured_status,effective_status,buying_type,"
    "bid_strategy,daily_budget,lifetime_budget,budget_remaining,spend_cap,"
    "special_ad_categories,special_ad_category_country,promoted_object,"
    "is_skadnetwork_attribution,start_time,stop_time,created_time,updated_time,"
    "account_id"
)


def get_campaigns(
    account_id: str = "",
    limit: int = 25,
    status_filter: str = "",
    fields: str = "",
    params: dict | None = None,
    extra: dict | None = None,
) -> str:
    """List campaigns for an ad account.

    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).
    status_filter: convenience for effective_status (e.g. 'ACTIVE'); pass a raw
                   `params={'effective_status':[...]}`/`filtering` for anything richer.
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    """
    p = dict(params or {})
    if status_filter:
        p.setdefault("effective_status", [status_filter])
    return _base.get(
        f"{acct(account_id)}/campaigns",
        _CAMPAIGN_FIELDS,
        fields=fields,
        params=p,
        limit=limit,
        extra=extra,
    )


def get_campaign_details(
    campaign_id: str, fields: str = "", extra: dict | None = None
) -> str:
    """Full detail for one campaign (generous default fields; override via `fields`)."""
    return _base.get(campaign_id, _CAMPAIGN_FIELDS, fields=fields, extra=extra)


def create_campaign(
    account_id: str = "",
    name: str = "",
    objective: str = "",
    status: str = "PAUSED",
    special_ad_categories: list | None = None,
    daily_budget: int | str | None = None,
    lifetime_budget: int | str | None = None,
    bid_strategy: str | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Create a campaign.

    objective: ANY value the Graph API accepts — the 6 OUTCOME_* values AND the
    15 legacy objectives are all forwarded as-is (NOT rejected; see
    rebuild/SCHEMA-VERIFICATION.md). special_ad_categories defaults to [] (API
    requires the key present). Convention: defaults to PAUSED. Anything not
    modeled here goes through `extra`.
    """
    body: dict = {
        "name": name,
        "objective": objective,
        "status": status,
        "special_ad_categories": special_ad_categories
        if special_ad_categories is not None
        else [],
    }
    if daily_budget is not None:
        body["daily_budget"] = daily_budget
    if lifetime_budget is not None:
        body["lifetime_budget"] = lifetime_budget
    if bid_strategy is not None:
        body["bid_strategy"] = bid_strategy
    return _base.write(
        f"{acct(account_id)}/campaigns",
        body,
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


def update_campaign(
    campaign_id: str,
    fields_to_update: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Update a campaign. Pass any updatable field in `fields_to_update` (or
    `extra`) — name, status, daily_budget, bid_strategy, objective, spend_cap,
    is_adset_budget_sharing_enabled, ... Nothing is gated; Graph rejects what it
    won't accept and that error is returned verbatim. Budget/status changes are
    financially material — preview with dry_run/validate_only first.
    """
    return _base.write(
        campaign_id,
        dict(fields_to_update or {}),
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


def delete_campaign(campaign_id: str, dry_run: bool = False) -> str:
    """Delete a campaign (prefer pausing — deletion loses learning/history)."""
    return _base.delete(campaign_id, dry_run=dry_run)


_TOOLS = [
    get_campaigns,
    get_campaign_details,
    create_campaign,
    update_campaign,
    delete_campaign,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

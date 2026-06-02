"""Ad set tools — thin, non-gating wrappers (see _base.py contract).

Same tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. Unlike the third-party: no fixed field allow-list, no
optimization_goal / billing_event / destination_type rejection, no bid_strategy
gating, and update_adset accepts ANY field (promoted_object, targeting,
attribution_spec, ...) — the exact gap this rebuild exists to fix.
"""

from .._account import acct
from . import _base

# Generous — surface fields the third-party hid (promoted_object,
# attribution_spec, destination_type, budget_remaining, bid_strategy, ...).
# Override via `fields`.
_ADSET_FIELDS = (
    "id,name,campaign_id,account_id,status,configured_status,effective_status,"
    "optimization_goal,billing_event,bid_amount,bid_strategy,daily_budget,"
    "lifetime_budget,budget_remaining,targeting,promoted_object,"
    "attribution_spec,destination_type,start_time,end_time,pacing_type,"
    "is_dynamic_creative,frequency_control_specs,created_time,updated_time"
)


def get_adsets(
    account_id: str = "",
    campaign_id: str = "",
    limit: int = 25,
    fields: str = "",
    params: dict | None = None,
    extra: dict | None = None,
) -> str:
    """List ad sets.

    campaign_id: if given, lists that campaign's ad sets ({campaign_id}/adsets);
                 otherwise lists the account's ad sets ({acct}/adsets).
    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT). Only used when
                campaign_id is not given.
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    """
    path = (
        f"{campaign_id}/adsets"
        if campaign_id
        else f"{acct(account_id)}/adsets"
    )
    return _base.get(
        path,
        _ADSET_FIELDS,
        fields=fields,
        params=params,
        limit=limit,
        extra=extra,
    )


def get_adset_details(
    adset_id: str, fields: str = "", extra: dict | None = None
) -> str:
    """Full detail for one ad set (generous default fields; override via `fields`)."""
    return _base.get(adset_id, _ADSET_FIELDS, fields=fields, extra=extra)


def create_adset(
    account_id: str = "",
    campaign_id: str = "",
    name: str = "",
    optimization_goal: str = "",
    billing_event: str = "",
    daily_budget: int | str | None = None,
    lifetime_budget: int | str | None = None,
    targeting: dict | None = None,
    promoted_object: dict | None = None,
    bid_amount: int | str | None = None,
    bid_strategy: str | None = None,
    status: str = "PAUSED",
    start_time: str | None = None,
    end_time: str | None = None,
    attribution_spec: list | dict | None = None,
    destination_type: str | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Create an ad set.

    optimization_goal / billing_event / destination_type: ANY value the Graph
    API accepts is forwarded as-is (NOT rejected). campaign_id is included in
    the body. targeting / promoted_object / attribution_spec are passed through
    as dict/list — the client auto-JSON-encodes them, so do NOT json.dumps
    yourself. Optional fields are only sent when not None. Convention: defaults
    to PAUSED. Anything not modeled here goes through `extra`.
    """
    body: dict = {
        "campaign_id": campaign_id,
        "name": name,
        "optimization_goal": optimization_goal,
        "billing_event": billing_event,
        "status": status,
    }
    if daily_budget is not None:
        body["daily_budget"] = daily_budget
    if lifetime_budget is not None:
        body["lifetime_budget"] = lifetime_budget
    if targeting is not None:
        body["targeting"] = targeting
    if promoted_object is not None:
        body["promoted_object"] = promoted_object
    if bid_amount is not None:
        body["bid_amount"] = bid_amount
    if bid_strategy is not None:
        body["bid_strategy"] = bid_strategy
    if start_time is not None:
        body["start_time"] = start_time
    if end_time is not None:
        body["end_time"] = end_time
    if attribution_spec is not None:
        body["attribution_spec"] = attribution_spec
    if destination_type is not None:
        body["destination_type"] = destination_type
    return _base.write(
        f"{acct(account_id)}/adsets",
        body,
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


def update_adset(
    adset_id: str,
    fields_to_update: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Update an ad set. Pass any updatable field in `fields_to_update` (or
    `extra`) — name, status, daily_budget, lifetime_budget, bid_amount,
    bid_strategy, optimization_goal, targeting, promoted_object,
    attribution_spec, frequency_control_specs, ... NOTHING is gated (no
    allow-list — this is the exact gap the rebuild exists to fix); dict/list
    values are auto-JSON-encoded by the client (do NOT json.dumps yourself).
    Graph rejects what it won't accept and that error is returned verbatim.
    Budget/status/targeting changes are financially material — preview with
    dry_run/validate_only first.
    """
    return _base.write(
        adset_id,
        dict(fields_to_update or {}),
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


def delete_adset(adset_id: str, dry_run: bool = False) -> str:
    """Delete an ad set (prefer pausing — deletion loses learning/history)."""
    return _base.delete(adset_id, dry_run=dry_run)


_TOOLS = [
    get_adsets,
    get_adset_details,
    create_adset,
    update_adset,
    delete_adset,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

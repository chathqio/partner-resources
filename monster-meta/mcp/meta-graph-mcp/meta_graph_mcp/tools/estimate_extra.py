"""Extra estimate tools — thin, non-gating wrappers (see _base.py contract).

Complements estimate.py (delivery_estimate via estimate_audience_size). These
expose the remaining reach / delivery / overlap edges (API-SURFACE.md §B5):
`{act_<id>}/delivery_estimate`, `/reachestimate`, `/audienceoverlap`. All
READ-only and non-gating.

Unlike the third-party meta-ads MCP: NO preflight gating (it refused unless
geo_locations / a custom audience were present and hid the result behind
reformatting) — the spec is forwarded verbatim and Graph's own error is
returned untouched, INCLUDING the `users: -1` case `reachestimate` returns when
the estimate is unsupported (e.g. PII custom audiences) and the
estimate_ready / estimate_dau diagnostics. dict/list args (targeting_spec,
promoted_object, custom_audiences) pass through as real objects (the client
encodes them; NOT json.dumps'd). These edges return their own payload shape
(no node-field selection), so `_base.get` is called with an empty
default_fields string and everything rides in `params`/`extra` (extra merged
last).
"""

from .._account import acct
from . import _base


def delivery_estimate(
    account_id: str = "",
    optimization_goal: str = "",
    targeting_spec: dict | None = None,
    promoted_object: dict | None = None,
    extra: dict | None = None,
) -> str:
    """Get a delivery estimate for a targeting spec + optimization goal.

    GET `{act_<id>}/delivery_estimate` — returns `{estimate_dau,
    estimate_mau_lower/upper_bound, bid_estimate:{min,median,max},
    estimate_ready}`. account_id: act_<id> (or empty to use
    META_DEFAULT_ACCOUNT).

    optimization_goal: e.g. REACH, LINK_CLICKS, IMPRESSIONS, OFFSITE_CONVERSIONS,
        CONVERSIONS, ... — forwarded as-is when given (never rejected).
    targeting_spec: the full targeting spec — sent as `targeting_spec` and
        passed through as a real object (the client encodes it; NOT
        json.dumps'd). NOT preflight-validated; Graph's own error (e.g. subcode
        1885364 "Missing Target Audience Location") is returned verbatim.
    promoted_object: e.g. {"pixel_id":"...","custom_event_type":"PURCHASE"} —
        passed through as a real object.
    extra: any additional query params, merged last (open passthrough).
    """
    p: dict = {}
    if optimization_goal:
        p["optimization_goal"] = optimization_goal
    if targeting_spec is not None:
        p["targeting_spec"] = targeting_spec
    if promoted_object is not None:
        p["promoted_object"] = promoted_object
    return _base.get(
        f"{acct(account_id)}/delivery_estimate",
        "",
        params=p,
        extra=extra,
    )


def reach_estimate(
    account_id: str = "",
    targeting_spec: dict | None = None,
    optimize_for: str = "",
    extra: dict | None = None,
) -> str:
    """Get a reach estimate for a targeting spec.

    GET `{act_<id>}/reachestimate` — returns `{users, bid_estimations,
    estimate_ready}`. account_id: act_<id> (or empty to use
    META_DEFAULT_ACCOUNT).

    targeting_spec: the full targeting spec — sent as `targeting_spec` and
        passed through as a real object (the client encodes it; NOT
        json.dumps'd). NOT preflight-validated; Graph's own error is returned
        verbatim. NOTE: `reachestimate` returns `users: -1` when the estimate
        is unsupported (e.g. PII custom audiences) — that response is surfaced
        verbatim, never reinterpreted as an error or rejection.
    optimize_for: forwarded as-is when given (never rejected).
    extra: any additional query params, merged last (open passthrough).
    """
    p: dict = {}
    if targeting_spec is not None:
        p["targeting_spec"] = targeting_spec
    if optimize_for:
        p["optimize_for"] = optimize_for
    return _base.get(
        f"{acct(account_id)}/reachestimate",
        "",
        params=p,
        extra=extra,
    )


def audience_overlap(
    account_id: str = "",
    custom_audiences: list | None = None,
    comparison_custom_audience_id: str = "",
    extra: dict | None = None,
) -> str:
    """Get the overlap between custom audiences.

    GET `{act_<id>}/audienceoverlap`. account_id: act_<id> (or empty to use
    META_DEFAULT_ACCOUNT).

    custom_audiences: a list of custom audience ids to compare — passed through
        as a real object (the client encodes it; NOT json.dumps'd) and never
        rejected.
    comparison_custom_audience_id: forwarded as-is when given. Nothing is
        preflight-validated; Graph's own error is returned verbatim.
    extra: any additional query params, merged last (open passthrough).
    """
    p: dict = {}
    if custom_audiences is not None:
        p["custom_audiences"] = custom_audiences
    if comparison_custom_audience_id:
        p["comparison_custom_audience_id"] = comparison_custom_audience_id
    return _base.get(
        f"{acct(account_id)}/audienceoverlap",
        "",
        params=p,
        extra=extra,
    )


_TOOLS = [
    delivery_estimate,
    reach_estimate,
    audience_overlap,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

"""Audience-estimate tool — thin, non-gating wrapper (see _base.py contract).

Same tool name as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. READ-only. Unlike the third-party: NO preflight gating (the
third-party refused unless geo_locations / a custom audience were present and
hid the result behind reformatting) — the targeting spec is forwarded verbatim
and Graph's own error is returned untouched. dict args (targeting,
promoted_object) pass through as real objects (the client encodes them; NOT
json.dumps'd). Anything not modeled is reachable via `extra` (merged last).
"""

from .._account import acct
from . import _base


def estimate_audience_size(
    account_id: str = "",
    targeting: dict | None = None,
    optimization_goal: str = "",
    promoted_object: dict | None = None,
    extra: dict | None = None,
) -> str:
    """Estimate audience size for a targeting spec.

    GET `{act_<id>}/delivery_estimate` — the same endpoint the third-party fell
    back to (it primarily hit reachestimate, which does not accept
    optimization_goal/promoted_object; delivery_estimate is the one that takes
    the full spec). account_id: act_<id> (or empty to use
    META_DEFAULT_ACCOUNT).

    targeting: the full targeting spec — demographics, geo_locations,
    flexible_spec, interests, behaviors, custom_audiences, ... — sent as the
    `targeting_spec` param and passed through as a real object (the client
    encodes it; NOT json.dumps'd). NOT preflight-validated: no location/custom-
    audience requirement is enforced here; Graph's own error (e.g. subcode
    1885364 "Missing Target Audience Location") is returned verbatim.
    optimization_goal: e.g. REACH, LINK_CLICKS, IMPRESSIONS, CONVERSIONS,
    OFFSITE_CONVERSIONS, ... — forwarded as-is when given (never rejected).
    promoted_object: e.g. {"pixel_id":"...","custom_event_type":"PURCHASE"} —
    passed through as a real object. extra: any additional query params, merged
    last (open passthrough).
    """
    p: dict = {}
    if targeting is not None:
        p["targeting_spec"] = targeting
    if optimization_goal:
        p["optimization_goal"] = optimization_goal
    if promoted_object is not None:
        p["promoted_object"] = promoted_object
    return _base.get(
        f"{acct(account_id)}/delivery_estimate",
        "",
        params=p,
        extra=extra,
    )


_TOOLS = [
    estimate_audience_size,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

"""Insights tools — thin, non-gating wrappers (see _base.py contract).

Same tool name as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. Unlike the third-party: NO fixed field allow-list (the third-party
hard-coded one field set and could not subset/extend it), every breakdown /
field / date_preset is forwarded as-is and never rejected, dict/list args
(time_range, filtering) pass through as real objects (the client encodes them;
NOT json.dumps'd), and anything not modeled here is reachable via `extra`.
"""

from . import _base

# Generous — surface the metrics the third-party hid behind a fixed list, plus
# conversion/value/ROAS columns and the date window. Override via `fields`.
_INSIGHTS_FIELDS = (
    "spend,impressions,reach,frequency,clicks,cpc,cpm,ctr,actions,"
    "action_values,conversions,conversion_values,cost_per_action_type,"
    "purchase_roas,date_start,date_stop"
)


def get_insights(
    object_id: str,
    level: str = "",
    date_preset: str = "last_7d",
    time_range: dict | None = None,
    fields: str = "",
    breakdowns: str = "",
    action_breakdowns: str = "",
    action_attribution_windows: str = "",
    filtering: list | None = None,
    time_increment: str = "",
    limit: int = 100,
    params: dict | None = None,
    extra: dict | None = None,
) -> str:
    """Get performance insights for an account, campaign, ad set or ad.

    GETs `{object_id}/insights`. object_id is any of act_<id>, a campaign id,
    an ad set id or an ad id.

    level: ad / adset / campaign / account — convenience for the `level` param.
    date_preset: any preset the Graph API accepts (today, yesterday, last_3d,
                 last_7d, last_14d, last_28d, last_30d, last_90d, this_month,
                 last_month, this_quarter, last_quarter, maximum, ...). NOT
                 validated — forwarded as-is. If `time_range` is given it takes
                 precedence and date_preset is dropped.
    time_range: a dict {"since":"YYYY-MM-DD","until":"YYYY-MM-DD"} — passed
                through as a real object (the client encodes it; NOT
                json.dumps'd).
    breakdowns / action_breakdowns: any breakdown dimension(s), comma-joined.
                EVERY breakdown is accepted (age, gender, country, region, dma,
                device_platform, publisher_platform, platform_position,
                impression_device, *_asset creative breakdowns, hourly_stats_*,
                product_id, ...). Nothing is rejected.
    action_attribution_windows: e.g. "1d_click,7d_click,1d_view" — forwarded
                as-is (string param; no quoting transform applied).
    filtering: a list of filter dicts, e.g.
               [{"field":"spend","operator":"GREATER_THAN","value":0}] — passed
               through as a real object (NOT json.dumps'd).
    time_increment: 1 (daily), 7, 28, monthly, all_days, ... — forwarded as-is.
    fields: override the (generous) default field list.
    params/extra: any additional query params, forwarded untouched; `extra`
                merges last (open passthrough).

    Async / large reports: the synchronous `/insights` GET can time out on big
    accounts. For async reporting, use the primitive `graph_call` to POST
    `{account}/insights` (returns a `report_run_id`), then poll that
    `{report_run_id}` for `async_status`. Per
    rebuild/SCHEMA-VERIFICATION.md the six exact async_status strings are:
    "Job Not Started", "Job Started", "Job Running", "Job Completed",
    "Job Failed", "Job Skipped". Fetch results from `{report_run_id}/insights`
    ONLY when async_status == "Job Completed" AND async_percent_completion ==
    100 ("Job Failed" -> review query & retry; "Job Skipped" -> expired,
    resubmit).
    """
    p: dict = {}
    if level:
        p["level"] = level
    if time_range is not None:
        p["time_range"] = time_range
    elif date_preset:
        p["date_preset"] = date_preset
    if breakdowns:
        p["breakdowns"] = breakdowns
    if action_breakdowns:
        p["action_breakdowns"] = action_breakdowns
    if action_attribution_windows:
        p["action_attribution_windows"] = action_attribution_windows
    if filtering is not None:
        p["filtering"] = filtering
    if time_increment:
        p["time_increment"] = time_increment
    p = _base.merge(p, params)
    return _base.get(
        f"{object_id}/insights",
        _INSIGHTS_FIELDS,
        fields=fields,
        params=p,
        limit=limit,
        extra=extra,
    )


_TOOLS = [
    get_insights,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

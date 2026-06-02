"""Async-insights tools — thin, non-gating wrappers (see _base.py contract).

The synchronous `/insights` GET (insights.py) times out on big accounts and
long windows. The async path is: POST `{object|act_<id>}/insights` ->
`{report_run_id}`; poll `GET /{report_run_id}` for `async_status` +
`async_percent_completion`; fetch results from `{report_run_id}/insights` ONLY
when `async_status == "Job Completed"` AND `async_percent_completion == 100`.

Per rebuild/SCHEMA-VERIFICATION.md §3 the six exact `async_status` strings are:
"Job Not Started", "Job Started", "Job Running", "Job Completed", "Job Failed",
"Job Skipped". "Job Failed" -> review query & retry; "Job Skipped" -> the
report expired, resubmit. 100% completion ALONE is insufficient — the status
must also be "Job Completed".

Unlike the third-party meta-ads MCP: NO fixed field allow-list, every breakdown
/ field / date_preset forwarded as-is and never rejected, dict/list args
(time_range, filtering) pass through as real objects (the client encodes them;
NOT json.dumps'd), and anything not modeled is reachable via `extra` (merged
last). The create POST still routes through `_base.write`; the poll wraps
`polling.poll_insights_report`; the status read routes through `_base.get`.
"""

from .._account import acct
from .. import polling
from . import _base

# Generous — surface the metrics the third-party hid behind a fixed list, plus
# conversion/value/ROAS columns and the date window. Override via `fields`.
_INSIGHTS_FIELDS = (
    "spend,impressions,reach,frequency,clicks,cpc,cpm,ctr,actions,"
    "action_values,conversions,conversion_values,cost_per_action_type,"
    "purchase_roas,date_start,date_stop"
)

# AdReportRun status fields — async_status + completion + the window the run
# covered. Override via `extra={"fields": "..."}` if needed.
_REPORT_RUN_FIELDS = (
    "async_status,async_percent_completion,date_start,date_stop"
)


def create_insights_report(
    object_id: str = "",
    account_id: str = "",
    level: str = "",
    fields: str = "",
    breakdowns: str = "",
    action_breakdowns: str = "",
    date_preset: str = "",
    time_range: dict | None = None,
    filtering: list | None = None,
    time_increment: str = "",
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Create an async insights report run.

    POSTs `{object_id}/insights` (async job) and returns the
    `{report_run_id}` envelope. Use `object_id` for a campaign / ad set / ad id
    (or an act_<id>); if `object_id` is empty the report is created against
    `{act_<account_id>}/insights` (account_id empty -> META_DEFAULT_ACCOUNT).

    Then poll with `poll_insights_report(report_run_id)` (or
    `get_report_run_status`): fetch results ONLY when `async_status == "Job
    Completed"` AND `async_percent_completion == 100`. The six exact
    async_status strings (rebuild/SCHEMA-VERIFICATION.md §3) are: "Job Not
    Started", "Job Started", "Job Running", "Job Completed", "Job Failed", "Job
    Skipped". "Job Failed" -> review query & retry; "Job Skipped" -> expired,
    resubmit. 100% completion ALONE is insufficient — the status must also be
    "Job Completed".

    fields: the metric/column list for the report (forwarded as-is; generous
            default if empty). Override freely — every field is accepted.
    level: ad / adset / campaign / account — convenience for the `level` param.
    date_preset: any preset the Graph API accepts (today, yesterday, last_7d,
                 last_14d, last_28d, last_30d, last_90d, this_month, last_month,
                 this_quarter, maximum, ...). NOT validated. If `time_range` is
                 given it takes precedence and date_preset is dropped.
    time_range: a dict {"since":"YYYY-MM-DD","until":"YYYY-MM-DD"} — passed
                through as a real object (the client encodes it; NOT
                json.dumps'd).
    breakdowns / action_breakdowns: any breakdown dimension(s), comma-joined;
                EVERY breakdown is accepted, nothing rejected.
    filtering: a list of filter dicts, e.g.
               [{"field":"spend","operator":"GREATER_THAN","value":0}] — passed
               through as a real object (NOT json.dumps'd).
    time_increment: 1 (daily), 7, 28, monthly, all_days, ... — forwarded as-is.
    extra: any additional body params, merged LAST (open passthrough).
    dry_run: preview the POST locally without sending it.
    """
    target = (object_id or "").strip() or acct(account_id)
    body: dict = {"fields": fields or _INSIGHTS_FIELDS}
    if level:
        body["level"] = level
    if breakdowns:
        body["breakdowns"] = breakdowns
    if action_breakdowns:
        body["action_breakdowns"] = action_breakdowns
    if time_range is not None:
        body["time_range"] = time_range
    elif date_preset:
        body["date_preset"] = date_preset
    if filtering is not None:
        body["filtering"] = filtering
    if time_increment:
        body["time_increment"] = time_increment
    return _base.write(
        f"{target}/insights",
        body,
        extra=extra,
        dry_run=dry_run,
    )


def poll_insights_report(
    report_run_id: str,
    max_wait_s: int = 120,
    interval_s: float = 3.0,
    fetch_results: bool = True,
) -> str:
    """Poll an async insights report run until terminal, then fetch results.

    Thin wrapper over polling.poll_insights_report. Polls
    `GET /{report_run_id}` for `async_status` + `async_percent_completion` and
    returns once the run is terminal. Results are fetched from
    `{report_run_id}/insights` (cursor-paged) ONLY when `async_status == "Job
    Completed"` AND `async_percent_completion == 100` — 100% completion alone is
    insufficient. The six exact async_status strings
    (rebuild/SCHEMA-VERIFICATION.md §3) are: "Job Not Started", "Job Started",
    "Job Running", "Job Completed", "Job Failed", "Job Skipped". "Job Failed" ->
    review query & retry; "Job Skipped" -> the report expired, resubmit.

    max_wait_s: stop polling after this many seconds (timeout is surfaced, not
                raised). interval_s: seconds between polls.
    fetch_results: when False, return as soon as the run is "Job Completed" &
                   100% WITHOUT fetching the result rows.
    """
    return _base.dump(
        polling.poll_insights_report(
            report_run_id,
            max_wait_s=max_wait_s,
            interval_s=interval_s,
            fetch_results=fetch_results,
        )
    )


def get_report_run_status(
    report_run_id: str, extra: dict | None = None
) -> str:
    """Get the status of an async insights report run (one poll, no fetch).

    GETs `{report_run_id}` with fields=async_status,async_percent_completion,
    date_start,date_stop. The six exact `async_status` strings
    (rebuild/SCHEMA-VERIFICATION.md §3) are: "Job Not Started", "Job Started",
    "Job Running", "Job Completed", "Job Failed", "Job Skipped". Fetch results
    from `{report_run_id}/insights` ONLY when `async_status == "Job Completed"`
    AND `async_percent_completion == 100` (100% completion ALONE is
    insufficient — the status must also be "Job Completed"). "Job Failed" ->
    review query & retry; "Job Skipped" -> expired, resubmit.

    extra: any additional query params, merged last (open passthrough; can
    override `fields`).
    """
    return _base.get(report_run_id, _REPORT_RUN_FIELDS, extra=extra)


_TOOLS = [
    create_insights_report,
    poll_insights_report,
    get_report_run_status,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

"""Misc tools — Ad Library, budget schedules, login link, generic search/fetch.

Thin, non-gating wrappers (see _base.py contract). Same tool names as the
third-party meta-ads MCP so the skill rewrite is a pure prefix swap. Unlike the
third-party: no required-arg rejections, no value allow-lists, every field
reachable via `extra`, and `get_login_link` is a static-token stub (this server
uses a long-lived META_ACCESS_TOKEN — no interactive OAuth).
"""

from . import _base

# Generous default — the public Ad Library fields the third-party requested,
# surfaced as-is. Override via `fields`.
_ADS_ARCHIVE_FIELDS = (
    "ad_creation_time,ad_creative_body,ad_creative_link_caption,"
    "ad_creative_link_description,ad_creative_link_title,"
    "ad_delivery_start_time,ad_delivery_stop_time,ad_snapshot_url,currency,"
    "demographic_distribution,funding_entity,impressions,page_id,page_name,"
    "publisher_platform,region_distribution,spend"
)

# Generous default for fetching an arbitrary node by id. Many of these only
# apply to certain node types — Graph silently drops the rest. Override freely.
_NODE_FIELDS = (
    "id,name,title,description,status,effective_status,objective,created_time,"
    "updated_time,start_time,stop_time,account_id,category,about,link,"
    "audience_size_lower_bound,audience_size_upper_bound,topic,path,disambiguation_category"
)


def search_ads_archive(
    search_terms: str = "",
    ad_reached_countries: list | None = None,
    limit: int = 25,
    fields: str = "",
    params: dict | None = None,
    extra: dict | None = None,
) -> str:
    """Search the public Facebook Ad Library archive (GET /ads_archive).

    search_terms: free-text query.
    ad_reached_countries: list of ISO country codes (e.g. ['US','GB']);
                          forwarded as-is (the client JSON-encodes lists).
    ad_type: defaults to 'ALL' (override via `params`/`extra`, e.g.
             'POLITICAL_AND_ISSUE_ADS', 'HOUSING_ADS').
    fields: override the (generous) default field list.
    params/extra: any additional query params, forwarded untouched.
    Nothing is rejected — missing/empty args are sent and Meta decides.
    """
    p: dict = {"search_terms": search_terms, "ad_type": "ALL"}
    if ad_reached_countries is not None:
        p["ad_reached_countries"] = ad_reached_countries
    p = _base.merge(p, params)
    return _base.get(
        "ads_archive",
        _ADS_ARCHIVE_FIELDS,
        fields=fields,
        params=p,
        limit=limit,
        extra=extra,
    )


def create_budget_schedule(
    campaign_id: str = "",
    budget_value: int = 0,
    budget_value_type: str = "",
    time_start: int = 0,
    time_end: int = 0,
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Create a budget schedule for a campaign (POST {campaign_id}/budget_schedules).

    Schedules a budget increase for an anticipated high-demand window. Times are
    Unix timestamps.

    budget_value: amount of the increase (interpreted per budget_value_type).
    budget_value_type: 'ABSOLUTE' or 'MULTIPLIER' — forwarded as-is, NOT
                       rejected; Graph validates and any error is returned verbatim.
    time_start / time_end: Unix timestamps for the high-demand window.
    extra: any additional body field, merged last.
    """
    body: dict = {
        "budget_value": budget_value,
        "budget_value_type": budget_value_type,
        "time_start": time_start,
        "time_end": time_end,
    }
    return _base.write(
        f"{campaign_id}/budget_schedules",
        body,
        extra=extra,
        dry_run=dry_run,
    )


def get_login_link(extra: dict | None = None) -> str:
    """Login-link status (no interactive OAuth in meta-graph-mcp).

    Kept so the skill's mcp__meta-graph__get_login_link reference still
    resolves. This server uses a static long-lived META_ACCESS_TOKEN from the
    .mcp.json env — there is no interactive login flow. Makes no API call.
    Run whoami() to check token validity/expiry.
    """
    return _base.dump(
        {
            "status": "static_token",
            "note": (
                "meta-graph-mcp uses a static long-lived META_ACCESS_TOKEN "
                "from .mcp.json env; no interactive login. Run whoami() to "
                "check token validity/expiry."
            ),
        }
    )


def search(query: str, extra: dict | None = None) -> str:
    """Generic Graph search (GET /search?q=...&type=...).

    A thin, non-gating search. `type` defaults to 'adinterest' (interest
    targeting research) and is overridable via `extra` (e.g.
    {'type':'adgeolocation'} / {'type':'page'} / {'type':'place'}). `fields`,
    `limit`, and any other search param are reachable via `extra`. Read-only;
    nothing filtered.
    """
    p: dict = {"q": query, "type": "adinterest"}
    return _base.get("search", "", params=p, extra=extra)


def fetch(id: str, extra: dict | None = None) -> str:
    """Fetch any Graph node by id (GET /{id}).

    Unlike the third-party 'fetch' (which only re-read a prior search cache),
    this hits the API directly for any node — account, campaign, ad set, ad,
    page, interest, etc. Generous default fields (irrelevant ones are silently
    dropped by Graph); override via `extra` ({'fields':'...'}). Read-only.
    """
    return _base.get(id, _NODE_FIELDS, extra=extra)


_TOOLS = [
    search_ads_archive,
    create_budget_schedule,
    get_login_link,
    search,
    fetch,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

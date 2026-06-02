"""Targeting-search tools — thin, non-gating wrappers (see _base.py contract).

Same tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. All READ-only: they hit the global `search` node with a `type`
param exactly as the third-party did. Unlike the third-party: nothing is
rejected (empty queries are forwarded — Graph returns its own error), list args
pass through as real objects (the client encodes them; NOT json.dumps'd), and
anything not modeled is reachable via `extra` (merged last).

These searches return their own payload shape (id/name/audience_size/path,
etc.); there is no node-field selection, so `_base.get` is called with an empty
default_fields string and everything rides in `params`/`extra`.
"""

from . import _base


def search_interests(
    query: str, limit: int = 25, extra: dict | None = None
) -> str:
    """Search interest targeting options by keyword.

    GET search?type=adinterest&q=<query>. query is forwarded as-is (never
    rejected). extra: any additional query params, merged last.
    """
    return _base.get(
        "search",
        "",
        params={"type": "adinterest", "q": query},
        limit=limit,
        extra=extra,
    )


def search_behaviors(limit: int = 50, extra: dict | None = None) -> str:
    """List behavior targeting options.

    GET search?type=adTargetingCategory&class=behaviors. extra: any additional
    query params, merged last (e.g. override `class`).
    """
    return _base.get(
        "search",
        "",
        params={"type": "adTargetingCategory", "class": "behaviors"},
        limit=limit,
        extra=extra,
    )


def search_demographics(limit: int = 50, extra: dict | None = None) -> str:
    """List demographic targeting options.

    GET search?type=adTargetingCategory&class=demographics. Pass a different
    class (life_events, industries, income, family_statuses, user_device,
    user_os, ...) via extra={"class": "..."} — extra merges last and wins.
    """
    return _base.get(
        "search",
        "",
        params={"type": "adTargetingCategory", "class": "demographics"},
        limit=limit,
        extra=extra,
    )


def search_geo_locations(
    query: str,
    location_types: list | None = None,
    limit: int = 25,
    extra: dict | None = None,
) -> str:
    """Search geographic targeting locations.

    GET search?type=adgeolocation&q=<query>. location_types (e.g.
    ["country","region","city","zip","geo_market","electoral_district"]) is
    passed through as a real object (the client encodes it; NOT json.dumps'd).
    query is forwarded as-is. extra: any additional query params, merged last.
    """
    p: dict = {"type": "adgeolocation", "q": query}
    if location_types is not None:
        p["location_types"] = location_types
    return _base.get("search", "", params=p, limit=limit, extra=extra)


def get_interest_suggestions(
    interest_list: list, limit: int = 25, extra: dict | None = None
) -> str:
    """Get interest suggestions based on existing interests.

    GET search?type=adinterestsuggestion&interest_list=<list>. interest_list
    (e.g. ["Basketball","Soccer"]) is passed through as a real object (the
    client encodes it; NOT json.dumps'd) and never rejected. extra: any
    additional query params, merged last.
    """
    return _base.get(
        "search",
        "",
        params={
            "type": "adinterestsuggestion",
            "interest_list": interest_list,
        },
        limit=limit,
        extra=extra,
    )


_TOOLS = [
    search_interests,
    search_behaviors,
    search_demographics,
    search_geo_locations,
    get_interest_suggestions,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

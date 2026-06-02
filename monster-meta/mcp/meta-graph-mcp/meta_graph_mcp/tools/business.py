"""Business asset tools — thin, non-gating wrappers (see _base.py contract).

Same tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. These are READ-only context lookups against a Business Manager.
Unlike the third-party: no field allow-list (generous defaults, overridable via
`fields`), every field reachable via `extra`, and the `asset` edge name is
forwarded VERBATIM — never validated against an allow-list, so any business
edge (modeled here or not) is reachable.

Business-scoped, so no `_account.acct` resolution here — the caller passes the
business id explicitly.
"""

from . import _base

# Generous default for asset-edge listings. Many of these only apply to certain
# asset types — Graph silently drops the rest. Override via `fields`.
_ASSET_FIELDS = (
    "id,name,account_id,account_status,business,category,about,link,"
    "access_type,permitted_tasks,is_created_by_business,currency,timezone_name"
)

# Generous default for system users on a business.
_SYSTEM_USER_FIELDS = "id,name,role,finance_permission,ip_permission"


def get_business_assets(
    business_id: str,
    asset: str = "owned_ad_accounts",
    limit: int = 100,
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """List a Business Manager's assets on a given edge.

    business_id: the Business Manager id.
    asset: the edge to read — owned_ad_accounts | client_ad_accounts |
           owned_pages | client_pages | owned_pixels |
           owned_product_catalogs | system_users (or ANY other business edge).
           Forwarded VERBATIM — NOT validated; an unmodeled edge is still tried
           and Graph returns its own error if it doesn't exist.
    limit: page size (default 100).
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched (merged last).
    """
    return _base.get(
        f"{business_id}/{asset}",
        _ASSET_FIELDS,
        fields=fields,
        limit=limit,
        extra=extra,
    )


def get_system_users(
    business_id: str, fields: str = "", extra: dict | None = None
) -> str:
    """List the system users on a Business Manager.

    business_id: the Business Manager id.
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    """
    return _base.get(
        f"{business_id}/system_users",
        _SYSTEM_USER_FIELDS,
        fields=fields,
        extra=extra,
    )


def get_page_access(page_id: str, extra: dict | None = None) -> str:
    """Page access details for ad ownership/promotion.

    Returns access_token,name,id,tasks for the page. The access_token is a
    page token — that is the caller's own asset (the auth'd user already has a
    role on this page), so returning it is fine. An ad's object_story_spec /
    promoted_object page_id must be a page the token has an admin/advertiser
    role on; `tasks` shows what this token can do.

    extra: any additional query params, forwarded untouched.
    """
    return _base.get(
        page_id,
        "access_token,name,id,tasks",
        extra=extra,
    )


_TOOLS = [
    get_business_assets,
    get_system_users,
    get_page_access,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

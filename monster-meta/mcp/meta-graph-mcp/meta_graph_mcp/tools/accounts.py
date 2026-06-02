"""Account & page tools — thin, non-gating wrappers (see _base.py contract).

Same tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. Unlike the third-party: no fixed field allow-list (it hid
spend_cap, balance, funding_source, capabilities, min_daily_budget, ...), no
cents->dollars mangling of amount_spent/balance, and no multi-approach page
"discovery" guesswork — pages come straight from the account's promote_pages
edge, with every field reachable via `fields`/`extra`.
"""

from .._account import acct
from . import _base

# Generous — surface fields the third-party hid (spend_cap, balance,
# funding_source, capabilities, min_daily_budget, business, ...). Override
# via `fields`. Note: amount_spent/balance are returned in the account's
# smallest currency unit (cents), NOT pre-converted — raw API values.
_ACCOUNT_FIELDS = (
    "id,name,account_id,account_status,disable_reason,amount_spent,spend_cap,"
    "balance,currency,timezone_name,timezone_id,business,funding_source,"
    "capabilities,min_daily_budget,created_time"
)

# Generous page field set — surface verification, tasks, picture, etc.
_PAGE_FIELDS = (
    "id,name,username,category,fan_count,link,verification_status,"
    "picture,tasks,access_token"
)


def get_ad_accounts(
    user_id: str = "me",
    limit: int = 200,
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """List ad accounts accessible by a user.

    user_id: Meta user ID or 'me' for the current user.
    limit: max accounts (default 200).
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    amount_spent/balance are raw API values (smallest currency unit, e.g.
    cents) — NOT pre-divided like the third-party did.
    """
    return _base.get(
        f"{user_id}/adaccounts",
        _ACCOUNT_FIELDS,
        fields=fields,
        limit=limit,
        extra=extra,
    )


def get_account_info(
    account_id: str = "",
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """Full detail for one ad account.

    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    """
    return _base.get(
        acct(account_id), _ACCOUNT_FIELDS, fields=fields, extra=extra
    )


def get_account_pages(
    account_id: str = "",
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """List the pages an ad account can promote.

    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.

    Uses the {account}/promote_pages Graph edge — the canonical list of pages
    promotable by the ad account. (The third-party stitched together
    me/accounts + owned_pages + client_pages + creative scraping; this returns
    the authoritative edge directly and stays non-gating.)
    """
    return _base.get(
        f"{acct(account_id)}/promote_pages",
        _PAGE_FIELDS,
        fields=fields,
        extra=extra,
    )


def search_pages_by_name(
    search_term: str,
    account_id: str = "",
    limit: int = 25,
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """Search the account's promotable pages by name.

    search_term: substring to match against the page name.
    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).
    limit: max pages (default 25).
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.

    Hits the {account}/promote_pages Graph edge and passes search_term through
    as a query param so Graph filters server-side; nothing is dropped locally.
    """
    params: dict = {"search_term": search_term}
    return _base.get(
        f"{acct(account_id)}/promote_pages",
        _PAGE_FIELDS,
        fields=fields,
        params=params,
        limit=limit,
        extra=extra,
    )


_TOOLS = [
    get_ad_accounts,
    get_account_info,
    get_account_pages,
    search_pages_by_name,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

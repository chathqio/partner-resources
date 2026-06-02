"""Extra targeting tools — thin, non-gating wrappers (see _base.py contract).

Complements targeting.py (which hits the global `search` node). These hit the
account-scoped browse/validate/sentence-line edges:
`{act_<id>}/targetingbrowse`, `/targetingvalidation`, `/targetingsentencelines`
(API-SURFACE.md §B4). All READ-only and non-gating.

Unlike the third-party meta-ads MCP: nothing is rejected (empty / unusual
inputs are forwarded — Graph returns its own error), dict/list args
(targeting_list, id_list, targeting_spec) pass through as real objects (the
client encodes them; NOT json.dumps'd), and anything not modeled is reachable
via `extra` (merged last). These edges return their own payload shape (no
node-field selection), so `_base.get` is called with an empty default_fields
string and everything rides in `params`/`extra`.
"""

from .._account import acct
from . import _base


def browse_targeting(
    account_id: str = "",
    limit: int = 200,
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """Browse the full targeting category tree for an ad account.

    GET `{act_<id>}/targetingbrowse` — the full interests / behaviors /
    demographics / life_events / industries / income / family_statuses tree.
    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).

    fields: override the (empty) default — this edge returns its own payload
            shape so nothing is selected by default; forwarded as-is.
    extra: any additional query params, merged last (open passthrough).
    """
    return _base.get(
        f"{acct(account_id)}/targetingbrowse",
        "",
        fields=fields,
        limit=limit,
        extra=extra,
    )


def validate_targeting(
    account_id: str = "",
    targeting_list: list | None = None,
    id_list: list | None = None,
    extra: dict | None = None,
) -> str:
    """Validate targeting interests / ids against an ad account.

    GET `{act_<id>}/targetingvalidation`. account_id: act_<id> (or empty to use
    META_DEFAULT_ACCOUNT).

    targeting_list: a list of targeting specs (e.g.
        [{"type":"interests","name":"Tennis"}]) — passed through as a real
        object (the client encodes it; NOT json.dumps'd) and never rejected.
    id_list: a list of targeting ids (e.g. [6003020834693]) — passed through as
        a real object. Either / both may be supplied; nothing is preflight-
        validated, Graph's own error is returned verbatim.
    extra: any additional query params, merged last (open passthrough).
    """
    p: dict = {}
    if targeting_list is not None:
        p["targeting_list"] = targeting_list
    if id_list is not None:
        p["id_list"] = id_list
    return _base.get(
        f"{acct(account_id)}/targetingvalidation",
        "",
        params=p,
        extra=extra,
    )


def targeting_sentence_lines(
    account_id: str = "",
    targeting_spec: dict | None = None,
    extra: dict | None = None,
) -> str:
    """Get human-readable targeting sentence lines for a targeting spec.

    GET `{act_<id>}/targetingsentencelines` — returns the plain-language lines
    Ads Manager shows ("People who live in ...", "Age 25-54", ...) plus an
    `estimated_audience_size`. account_id: act_<id> (or empty to use
    META_DEFAULT_ACCOUNT).

    targeting_spec: the full targeting spec — sent as the `targeting_spec`
        param and passed through as a real object (the client encodes it; NOT
        json.dumps'd). NOT preflight-validated; Graph's own error is returned
        verbatim.
    extra: any additional query params, merged last (open passthrough).
    """
    p: dict = {}
    if targeting_spec is not None:
        p["targeting_spec"] = targeting_spec
    return _base.get(
        f"{acct(account_id)}/targetingsentencelines",
        "",
        params=p,
        extra=extra,
    )


_TOOLS = [
    browse_targeting,
    validate_targeting,
    targeting_sentence_lines,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

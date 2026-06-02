"""Audience tools — thin, non-gating wrappers (see _base.py contract).

Custom audiences, lookalikes, saved audiences, and the PII `users` edge. Same
tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. Raw PII is normalized+hashed locally (meta_graph_mcp.hashing)
BEFORE any request leaves the process; no subtype/schema is ever rejected.
"""

from .._account import acct
from ..client import request as _request
from . import _base
from .. import hashing

# Generous — surface the read-only diagnostics the third-party hid
# (operation_status, delivery_status, approximate_count, ...). Override via
# `fields`.
_CA_FIELDS = (
    "id,account_id,name,description,subtype,operation_status,delivery_status,"
    "approximate_count_lower_bound,"
    "approximate_count_upper_bound,data_source,customer_file_source,"
    "retention_days,rule,rule_aggregation,pixel_id,event_source_group,"
    "origin_audience_id,lookalike_spec,lookalike_audience_ids,is_value_based,"
    "permission_for_actions,time_created,time_updated,time_content_updated"
)

_SAVED_AUDIENCE_FIELDS = (
    "id,account_id,name,description,targeting,run_status,sentence_lines,"
    "approximate_count_lower_bound,approximate_count_upper_bound,time_created,"
    "time_updated"
)


def get_custom_audiences(
    account_id: str = "",
    limit: int = 25,
    fields: str = "",
    params: dict | None = None,
    extra: dict | None = None,
) -> str:
    """List custom audiences for an ad account.

    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).
    fields: override the (generous) default field list.
    params: any extra query params (filtering, etc.), forwarded untouched.
    extra: any additional query params, forwarded untouched.
    """
    return _base.get(
        f"{acct(account_id)}/customaudiences",
        _CA_FIELDS,
        fields=fields,
        params=params,
        limit=limit,
        extra=extra,
    )


def get_custom_audience(
    audience_id: str, fields: str = "", extra: dict | None = None
) -> str:
    """Full detail for one custom audience (generous default fields incl.
    operation_status / delivery_status; override via `fields`)."""
    return _base.get(audience_id, _CA_FIELDS, fields=fields, extra=extra)


def create_custom_audience(
    account_id: str = "",
    name: str = "",
    subtype: str = "",
    customer_file_source: str = "",
    description: str = "",
    rule: dict | list | None = None,
    retention_days: int | None = None,
    prefill: bool | None = None,
    pixel_id: str = "",
    origin_audience_id: str = "",
    lookalike_spec: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Create a custom audience.

    subtype: ANY value the Graph API accepts (CUSTOM, WEBSITE, APP,
    OFFLINE_CONVERSION, ENGAGEMENT, LOOKALIKE, CLAIM, MANAGED, VIDEO, ...) — NOT
    rejected. Fields are added only when truthy / not-None so the body stays
    minimal; `rule`/`lookalike_spec` are passed as objects (the client
    encodes). Anything not modeled here goes through `extra`.
    """
    body: dict = {"name": name}
    if subtype:
        body["subtype"] = subtype
    if customer_file_source:
        body["customer_file_source"] = customer_file_source
    if description:
        body["description"] = description
    if rule is not None:
        body["rule"] = rule
    if retention_days is not None:
        body["retention_days"] = retention_days
    if prefill is not None:
        body["prefill"] = prefill
    if pixel_id:
        body["pixel_id"] = pixel_id
    if origin_audience_id:
        body["origin_audience_id"] = origin_audience_id
    if lookalike_spec is not None:
        body["lookalike_spec"] = lookalike_spec
    return _base.write(
        f"{acct(account_id)}/customaudiences",
        body,
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


def update_custom_audience(
    audience_id: str,
    fields_to_update: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Update a custom audience. Pass any updatable field in `fields_to_update`
    (or `extra`) — name, description, retention_days, rule, opt_out_link, ...
    Nothing is gated; Graph rejects what it won't accept and that error is
    returned verbatim.
    """
    return _base.write(
        audience_id,
        dict(fields_to_update or {}),
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


def delete_custom_audience(audience_id: str, dry_run: bool = False) -> str:
    """Delete a custom audience (lookalikes built off it may also be removed)."""
    return _base.delete(audience_id, dry_run=dry_run)


def add_users_to_audience(
    audience_id: str,
    schema,
    data: list,
    is_raw: bool = True,
    app_ids: list | None = None,
    session: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Add users to a custom audience (`POST /{ca_id}/users`).

    schema: a single key string (e.g. 'EMAIL') or a list of keys (multi-key).
    data:   list of scalars (single-key) or list of row-lists (multi-key).
    is_raw: True (default) → normalize + SHA256-hash PII locally via
            meta_graph_mcp.hashing BEFORE building the payload, so raw PII
            never leaves this process. False → caller pre-hashed; pass through.
    app_ids / session: forwarded when given (batched/sessioned uploads).
    extra: any additional body fields, forwarded untouched.
    """
    transformed = (
        hashing.hash_ca_users(schema, data) if is_raw else data
    )
    payload: dict = {"schema": schema, "data": transformed}
    body: dict = {"payload": payload}
    if app_ids is not None:
        body["app_ids"] = app_ids
    if session is not None:
        body["session"] = session
    return _base.write(f"{audience_id}/users", body, extra=extra, dry_run=dry_run)


def remove_users_from_audience(
    audience_id: str,
    schema,
    data: list,
    is_raw: bool = True,
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Remove users from a custom audience (`DELETE /{ca_id}/users`).

    Same local normalize + SHA256 hashing as add_users_to_audience when
    is_raw=True (raw PII never leaves the process). DELETE-with-body is not
    available through _base, so this routes the one explicit
    client.request("DELETE", ..., body=...) call; still fully non-gating.
    """
    transformed = (
        hashing.hash_ca_users(schema, data) if is_raw else data
    )
    body: dict = {"payload": {"schema": schema, "data": transformed}}
    body = _base.merge(body, extra)
    return _base.dump(
        _request(
            "DELETE", f"{audience_id}/users", body=body, dry_run=dry_run
        )
    )


def create_lookalike(
    account_id: str = "",
    name: str = "",
    origin_audience_id: str = "",
    country: str = "",
    ratio: float | None = None,
    type: str = "",
    lookalike_spec: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Create a lookalike audience (`POST /act_{id}/customaudiences` with
    subtype=LOOKALIKE).

    If `lookalike_spec` is not given explicitly it is assembled from country /
    ratio / type (only truthy / not-None parts are included); an explicit
    `lookalike_spec` is passed through verbatim. Objects are encoded by the
    client. Nothing is gated.
    """
    body: dict = {"name": name, "subtype": "LOOKALIKE"}
    if origin_audience_id:
        body["origin_audience_id"] = origin_audience_id
    if lookalike_spec is not None:
        spec = lookalike_spec
    else:
        spec = {}
        if country:
            spec["country"] = country
        if ratio is not None:
            spec["ratio"] = ratio
        if type:
            spec["type"] = type
    body["lookalike_spec"] = spec
    return _base.write(
        f"{acct(account_id)}/customaudiences",
        body,
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


def get_saved_audiences(
    account_id: str = "",
    limit: int = 25,
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """List saved audiences for an ad account.

    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    """
    return _base.get(
        f"{acct(account_id)}/saved_audiences",
        _SAVED_AUDIENCE_FIELDS,
        fields=fields,
        limit=limit,
        extra=extra,
    )


def create_saved_audience(
    account_id: str = "",
    name: str = "",
    targeting: dict | None = None,
    description: str = "",
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Create a saved audience (`POST /act_{id}/saved_audiences`).

    `targeting` is the full targeting spec, passed as an object (the client
    encodes). Fields are added only when truthy / not-None. Anything not
    modeled here goes through `extra`.
    """
    body: dict = {"name": name}
    if targeting is not None:
        body["targeting"] = targeting
    if description:
        body["description"] = description
    return _base.write(
        f"{acct(account_id)}/saved_audiences",
        body,
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


_TOOLS = [
    get_custom_audiences,
    get_custom_audience,
    create_custom_audience,
    update_custom_audience,
    delete_custom_audience,
    add_users_to_audience,
    remove_users_from_audience,
    create_lookalike,
    get_saved_audiences,
    create_saved_audience,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

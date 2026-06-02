"""Ad creative tools — thin, non-gating wrappers (see _base.py contract).

Same tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. Unlike the third-party: no fixed field allow-list, all spec args
(object_story_spec, asset_feed_spec, degrees_of_freedom_spec, ...) are
forwarded as real objects (not json.dumps'd), every field reachable via
`extra`.
"""

from .._account import acct
from . import _base

# Generous — surface fields the third-party hid (effective_object_story_id,
# image_hash, instagram_actor_id, product_set_id, object_type, status, ...).
# Override via `fields`.
_CREATIVE_FIELDS = (
    "id,name,account_id,object_story_spec,object_story_id,"
    "effective_object_story_id,asset_feed_spec,degrees_of_freedom_spec,body,"
    "title,image_hash,image_url,thumbnail_url,call_to_action_type,url_tags,"
    "instagram_actor_id,product_set_id,object_type,status"
)


def get_ad_creatives(
    account_id: str = "",
    ad_id: str = "",
    limit: int = 25,
    fields: str = "",
    params: dict | None = None,
    extra: dict | None = None,
) -> str:
    """List ad creatives, optionally scoped to a single ad.

    ad_id: list creatives attached to one ad (uses {ad_id}/adcreatives).
    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT); used only when
                ad_id is not given (uses {account_id}/adcreatives).
    fields: override the (generous) default field list.
    params/extra: any additional query params, forwarded untouched.
    """
    if ad_id:
        path = f"{ad_id}/adcreatives"
    else:
        path = f"{acct(account_id)}/adcreatives"
    return _base.get(
        path,
        _CREATIVE_FIELDS,
        fields=fields,
        params=params,
        limit=limit,
        extra=extra,
    )


def get_creative_details(
    creative_id: str, fields: str = "", extra: dict | None = None
) -> str:
    """Full detail for one creative (generous default fields; override via `fields`)."""
    return _base.get(creative_id, _CREATIVE_FIELDS, fields=fields, extra=extra)


def create_ad_creative(
    account_id: str = "",
    name: str = "",
    object_story_spec: dict | None = None,
    object_story_id: str | None = None,
    asset_feed_spec: dict | None = None,
    degrees_of_freedom_spec: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Create an ad creative.

    object_story_spec / asset_feed_spec / degrees_of_freedom_spec are forwarded
    as real objects (the client encodes them; NOT json.dumps'd).
    object_story_id references an existing page post. Anything not modeled here
    (image_hash, url_tags, instagram_actor_id, call_to_action_type, ...) goes
    through `extra` and nothing is gated.
    """
    body: dict = {"name": name}
    if object_story_spec is not None:
        body["object_story_spec"] = object_story_spec
    if object_story_id is not None:
        body["object_story_id"] = object_story_id
    if asset_feed_spec is not None:
        body["asset_feed_spec"] = asset_feed_spec
    if degrees_of_freedom_spec is not None:
        body["degrees_of_freedom_spec"] = degrees_of_freedom_spec
    return _base.write(
        f"{acct(account_id)}/adcreatives",
        body,
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


def update_ad_creative(
    creative_id: str,
    fields_to_update: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
    validate_only: bool = False,
) -> str:
    """Update an ad creative. Pass any updatable field in `fields_to_update`
    (or `extra`) — name, asset_feed_spec, degrees_of_freedom_spec,
    creative_features_spec, ... Nothing is gated and there is no allow-list;
    pass spec values as real objects (the client encodes them). The Meta API
    itself limits which fields are mutable on an existing creative — that
    boundary is enforced by Graph (its error is returned verbatim), not by this
    wrapper. Preview with dry_run/validate_only first.
    """
    return _base.write(
        creative_id,
        dict(fields_to_update or {}),
        extra=extra,
        dry_run=dry_run,
        validate_only=validate_only,
    )


_TOOLS = [
    get_ad_creatives,
    get_creative_details,
    create_ad_creative,
    update_ad_creative,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

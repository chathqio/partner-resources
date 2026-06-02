"""Ad preview tools — thin, non-gating wrappers (see _base.py contract).

Same tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. Unlike the third-party: no field allow-list, the `creative` /
`dynamic_creative_spec` objects are forwarded as native objects (NOT
json.dumps'd), and `ad_format` is never pre-rejected — Graph requires it for the
account/creative path, so we pass it through untouched and let Graph return its
own error if it's missing or unknown.

Previews are READ-only. The returned AdPreview `body` is an <iframe> HTML
snippet whose URL is time-limited (~24h) — regenerate, don't cache.
"""

from .._account import acct
from . import _base


def generate_preview(
    account_id: str = "",
    ad_id: str = "",
    creative_id: str = "",
    creative: dict | None = None,
    ad_format: str = "",
    product_item_ids: list | None = None,
    dynamic_creative_spec: dict | None = None,
    extra: dict | None = None,
) -> str:
    """Generate a rendered ad preview (iframe HTML) for a placement.

    Three modes, picked by which id is supplied:
      - ad_id        -> GET {ad_id}/previews
      - creative_id  -> GET {creative_id}/previews
      - else         -> GET {act_<account>}/generatepreviews with `creative`

    ad_id/creative_id: preview an existing ad or creative.
    account_id: act_<id> (or empty -> META_DEFAULT_ACCOUNT); only used for the
                generatepreviews path.
    creative: an inline creative spec (object — forwarded as-is, NOT serialized);
              required by Graph for the generatepreviews path.
    ad_format: placement enum (MOBILE_FEED_STANDARD, DESKTOP_FEED_STANDARD,
               INSTAGRAM_STANDARD, INSTAGRAM_STORY, INSTAGRAM_REELS,
               FACEBOOK_STORY_MOBILE, AUDIENCE_NETWORK_*, MESSENGER_*,
               RIGHT_COLUMN_STANDARD, ...). Graph requires this for the
               account/creative path — it is forwarded untouched and NOT
               pre-rejected if blank; Graph returns its own error.
    product_item_ids: optional product item ids for DPA/catalog previews.
    dynamic_creative_spec: optional dynamic-creative spec (object — forwarded
                           as-is, NOT serialized).
    extra: any additional query params, forwarded untouched (merged last).
    """
    params: dict = {}
    if ad_format:
        params["ad_format"] = ad_format
    if creative is not None:
        params["creative"] = creative
    if product_item_ids is not None:
        params["product_item_ids"] = product_item_ids
    if dynamic_creative_spec is not None:
        params["dynamic_creative_spec"] = dynamic_creative_spec

    if ad_id:
        path = f"{ad_id}/previews"
    elif creative_id:
        path = f"{creative_id}/previews"
    else:
        path = f"{acct(account_id)}/generatepreviews"

    return _base.get(path, "", params=params, extra=extra)


_TOOLS = [
    generate_preview,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

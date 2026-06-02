"""Creative asset tools — thin, non-gating wrappers (see _base.py contract).

Same tool names as the third-party meta-ads MCP so the skill rewrite is a pure
prefix swap. Unlike the third-party: no fixed field allow-list (it hid
permalink_url, original_width/height, creatives, ...), get_ad_image/get_ad_video
return raw Graph JSON (not a downloaded/re-encoded binary), and upload_ad_image
routes through the single non-gating write path.

upload_ad_image note: Meta's /adimages accepts a base64 `bytes` field as an
alternative to a multipart file part, so we read the file, base64-encode it,
and route through _base.write (form-encoded) — no httpx / multipart needed.
"""

import base64
import os

from .._account import acct
from . import _base

# Generous — surface fields the third-party hid (permalink_url,
# original_width/height, creatives, is_associated_creatives_in_adgroups, ...).
# Override via `fields`.
_IMAGE_FIELDS = (
    "hash,name,url,permalink_url,width,height,original_width,original_height,"
    "status,creatives,is_associated_creatives_in_adgroups,created_time,"
    "updated_time"
)

# Generous video field set — source URL, thumbnails, metadata.
_VIDEO_FIELDS = (
    "id,source,title,description,length,picture,thumbnails,status,"
    "created_time,updated_time,permalink_url"
)


def get_ad_image(
    account_id: str = "",
    hashes: list | None = None,
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """List ad images for an account (optionally filtered by hash).

    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).
    hashes: optional list of image hashes to filter to; forwarded as the
            Graph `hashes` param. Omit to list all account images.
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    """
    params: dict = {}
    if hashes is not None:
        params["hashes"] = hashes
    return _base.get(
        f"{acct(account_id)}/adimages",
        _IMAGE_FIELDS,
        fields=fields,
        params=params,
        extra=extra,
    )


def get_ad_video(
    video_id: str, fields: str = "", extra: dict | None = None
) -> str:
    """Full detail for one ad video (source URL, thumbnails, metadata).

    video_id: the Meta video ID (get it from get_ad_creatives / asset_feed_spec).
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    """
    return _base.get(video_id, _VIDEO_FIELDS, fields=fields, extra=extra)


def upload_ad_image(
    account_id: str = "",
    image_path: str = "",
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Upload an image to an ad account's image library.

    account_id: act_<id> (or empty to use META_DEFAULT_ACCOUNT).
    image_path: local filesystem path to the image to upload.
    extra: any additional body fields (e.g. {'name': 'hero.jpg'}), merged last.
    dry_run: preview the request locally without calling Meta.

    The file is base64-encoded and sent as Meta's `bytes` field on /adimages
    (the documented alternative to a multipart file part), so this stays on the
    single non-gating write path. Returns a clear JSON note (not an exception)
    if image_path is missing or unreadable.
    """
    if not image_path:
        return _base.dump(
            {
                "note": "image_path is required",
                "detail": "Pass image_path=<local file path>; the file is "
                "base64-encoded into Meta's /adimages `bytes` field.",
            }
        )
    if not os.path.isfile(image_path):
        return _base.dump(
            {
                "note": "image file not found",
                "detail": f"No readable file at {image_path}",
                "image_path": image_path,
            }
        )
    try:
        with open(image_path, "rb") as fh:
            raw = fh.read()
    except OSError as exc:
        return _base.dump(
            {
                "note": "could not read image file",
                "detail": str(exc),
                "image_path": image_path,
            }
        )

    body: dict = {
        "bytes": base64.b64encode(raw).decode(),
        "name": os.path.basename(image_path),
    }
    return _base.write(
        f"{acct(account_id)}/adimages",
        body,
        extra=extra,
        dry_run=dry_run,
    )


_TOOLS = [
    get_ad_image,
    get_ad_video,
    upload_ad_image,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

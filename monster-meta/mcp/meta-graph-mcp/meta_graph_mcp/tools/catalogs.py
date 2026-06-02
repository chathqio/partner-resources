"""Catalog / commerce tools — thin, non-gating wrappers (see _base.py contract).

Same tool names / shape as the rest of the rewrite so the skill is a pure
prefix swap. Unlike the third-party: no fixed field allow-list, the `filter`
predicate and `schedule` are forwarded as real objects (the client encodes
them; NOT json.dumps'd), every field reachable via `extra`. These edges are
business/catalog/feed scoped — no ad-account scoping is applied.
"""

from . import _base

# Generous — surface fields the third-party hid (vertical, product_count,
# feed_count, da_display_settings, default_image_url, ...). Override via `fields`.
_CATALOG_FIELDS = (
    "id,name,vertical,product_count,feed_count,da_display_settings,"
    "default_image_url,fallback_image_url,is_catalog_segment,"
    "store_catalog_settings"
)

# Generous product field set — IDs, availability, pricing, imagery, links.
_PRODUCT_FIELDS = (
    "id,retailer_id,name,description,availability,condition,price,"
    "sale_price,currency,brand,category,product_type,url,image_url,"
    "additional_image_urls,gtin,mpn,custom_label_0,product_group,"
    "review_status,visibility"
)


def get_catalogs(
    business_id: str = "",
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """List product catalogs owned by a business.

    business_id: the Business Manager ID that owns the catalogs.
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    """
    return _base.get(
        f"{business_id}/owned_product_catalogs",
        _CATALOG_FIELDS,
        fields=fields,
        extra=extra,
    )


def get_catalog(
    catalog_id: str, fields: str = "", extra: dict | None = None
) -> str:
    """Full detail for one product catalog (generous default fields; override
    via `fields`)."""
    return _base.get(
        catalog_id,
        "name,vertical,product_count,feed_count",
        fields=fields,
        extra=extra,
    )


def create_catalog(
    business_id: str = "",
    name: str = "",
    vertical: str = "commerce",
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Create a product catalog under a business.

    vertical: ANY value the Graph API accepts —
    commerce|hotels|flights|destinations|home_listings|vehicles|... are all
    forwarded as-is (NOT rejected). Convention default: commerce. Anything not
    modeled here goes through `extra`.
    """
    body: dict = {"name": name, "vertical": vertical}
    return _base.write(
        f"{business_id}/owned_product_catalogs",
        body,
        extra=extra,
        dry_run=dry_run,
    )


def get_products(
    catalog_id: str,
    limit: int = 50,
    fields: str = "",
    params: dict | None = None,
    extra: dict | None = None,
) -> str:
    """List products in a catalog.

    fields: override the (generous) default field list.
    params/extra: any additional query params (e.g. a `filter` predicate),
                  forwarded untouched.
    """
    return _base.get(
        f"{catalog_id}/products",
        _PRODUCT_FIELDS,
        fields=fields,
        params=params,
        limit=limit,
        extra=extra,
    )


def create_product_set(
    catalog_id: str,
    name: str = "",
    filter: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Create a product set inside a catalog.

    filter: the product-set predicate, forwarded as a real object (the client
    encodes it; NOT json.dumps'd). Omit for a set that matches all products.
    Anything not modeled here goes through `extra` and nothing is gated.
    """
    body: dict = {"name": name}
    if filter is not None:
        body["filter"] = filter
    return _base.write(
        f"{catalog_id}/product_sets",
        body,
        extra=extra,
        dry_run=dry_run,
    )


def create_product_feed(
    catalog_id: str,
    name: str = "",
    schedule: dict | None = None,
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Create a product feed inside a catalog.

    schedule: the fetch schedule, forwarded as a real object (the client
    encodes it; NOT json.dumps'd). Anything not modeled here (update_schedule,
    default_currency, quoted_fields_mode, ...) goes through `extra` and nothing
    is gated.
    """
    body: dict = {"name": name}
    if schedule is not None:
        body["schedule"] = schedule
    return _base.write(
        f"{catalog_id}/product_feeds",
        body,
        extra=extra,
        dry_run=dry_run,
    )


def upload_product_feed(
    product_feed_id: str,
    url: str = "",
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Trigger an upload for a product feed.

    url: the feed source URL to fetch. Anything not modeled here goes through
    `extra` and nothing is gated.
    """
    body: dict = {"url": url}
    return _base.write(
        f"{product_feed_id}/uploads",
        body,
        extra=extra,
        dry_run=dry_run,
    )


_TOOLS = [
    get_catalogs,
    get_catalog,
    create_catalog,
    get_products,
    create_product_set,
    create_product_feed,
    upload_product_feed,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

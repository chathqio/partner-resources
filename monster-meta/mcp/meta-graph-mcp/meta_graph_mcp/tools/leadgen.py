"""Lead-gen tools — thin, non-gating wrappers (see _base.py contract).

Same tool names / shape as the rest of the rewrite so the skill is a pure
prefix swap. Unlike the third-party: no fixed field allow-list, the
questions/privacy_policy/context_card/thank_you_page specs are forwarded as
real objects (the client encodes them; NOT json.dumps'd), every field
reachable via `extra`. These edges are page/form scoped — no ad-account
scoping is applied. Reading leads requires `leads_retrieval` + a page access
token; Graph returns that error verbatim (this wrapper never gates).
"""

from . import _base

# Generous — surface fields the third-party hid (questions, leads_count,
# context_card, privacy_policy, follow_up_action_url, ...). Override via
# `fields`.
_FORM_FIELDS = (
    "id,name,status,questions,leads_count,created_time,context_card,"
    "privacy_policy,follow_up_action_url,thank_you_page,locale,page,"
    "expired_leads_count,organic_leads_count,question_page_custom_headline,"
    "block_display_for_non_targeted_viewer,is_optimized_for_quality"
)

# Generous lead field set — IDs, attribution, the field_data payload.
_LEAD_FIELDS = (
    "id,created_time,ad_id,adset_id,campaign_id,form_id,field_data,"
    "is_organic,partner_name,ad_name,adset_name,campaign_name,"
    "platform,retailer_item_id,custom_disclaimer_responses"
)


def get_leadgen_forms(
    page_id: str,
    limit: int = 50,
    fields: str = "",
    extra: dict | None = None,
) -> str:
    """List lead-gen forms on a page.

    page_id: the Facebook Page ID that owns the forms.
    fields: override the (generous) default field list.
    extra: any additional query params, forwarded untouched.
    """
    return _base.get(
        f"{page_id}/leadgen_forms",
        _FORM_FIELDS,
        fields=fields,
        limit=limit,
        extra=extra,
    )


def get_leadgen_form(
    form_id: str, fields: str = "", extra: dict | None = None
) -> str:
    """Full detail for one lead-gen form (generous default fields; override via
    `fields`)."""
    return _base.get(form_id, _FORM_FIELDS, fields=fields, extra=extra)


def create_leadgen_form(
    page_id: str,
    name: str = "",
    questions: list | None = None,
    privacy_policy: dict | None = None,
    context_card: dict | None = None,
    follow_up_action_url: str = "",
    thank_you_page: dict | None = None,
    locale: str = "",
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Create a lead-gen form on a page.

    questions / privacy_policy / context_card / thank_you_page are forwarded as
    real objects (the client encodes them; NOT json.dumps'd). Anything not
    modeled here (block_display_for_non_targeted_viewer, tracking_parameters,
    question_page_custom_headline, ...) goes through `extra` and nothing is
    gated.
    """
    body: dict = {"name": name}
    if questions is not None:
        body["questions"] = questions
    if privacy_policy is not None:
        body["privacy_policy"] = privacy_policy
    if context_card is not None:
        body["context_card"] = context_card
    if follow_up_action_url:
        body["follow_up_action_url"] = follow_up_action_url
    if thank_you_page is not None:
        body["thank_you_page"] = thank_you_page
    if locale:
        body["locale"] = locale
    return _base.write(
        f"{page_id}/leadgen_forms",
        body,
        extra=extra,
        dry_run=dry_run,
    )


def get_leads(
    form_id: str = "",
    ad_id: str = "",
    leadgen_id: str = "",
    limit: int = 100,
    fields: str = "",
    params: dict | None = None,
    extra: dict | None = None,
) -> str:
    """Retrieve leads.

    leadgen_id: read a single lead node directly ({leadgen_id}).
    form_id / ad_id: list leads under a form or ad ({form_id|ad_id}/leads).
    Resolution order: leadgen_id wins, else form_id, else ad_id.
    fields: override the (generous) default field list.
    params/extra: any additional query params (e.g. a `filtering` predicate),
                  forwarded untouched. Reading leads needs `leads_retrieval` +
                  a page access token — Graph's error is returned verbatim.
    """
    if leadgen_id:
        return _base.get(
            leadgen_id, _LEAD_FIELDS, fields=fields, params=params, extra=extra
        )
    return _base.get(
        f"{form_id or ad_id}/leads",
        _LEAD_FIELDS,
        fields=fields,
        params=params,
        limit=limit,
        extra=extra,
    )


def create_test_lead(
    form_id: str,
    extra: dict | None = None,
    dry_run: bool = False,
) -> str:
    """Create a test lead for a form (development/QA — does not consume real
    lead quota). Anything not modeled here goes through `extra` and nothing is
    gated.
    """
    return _base.write(
        f"{form_id}/test_leads",
        {},
        extra=extra,
        dry_run=dry_run,
    )


_TOOLS = [
    get_leadgen_forms,
    get_leadgen_form,
    create_leadgen_form,
    get_leads,
    create_test_lead,
]


def register(mcp) -> None:
    for fn in _TOOLS:
        mcp.tool()(fn)

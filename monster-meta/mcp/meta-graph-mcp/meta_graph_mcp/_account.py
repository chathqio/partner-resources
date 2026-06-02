"""Ad-account id resolution shared by named tools."""

from .client import DEFAULT_ACCOUNT


def acct(account_id: str = "") -> str:
    """Normalize an ad-account id.

    - empty -> META_DEFAULT_ACCOUNT (if set; else a clear error string the
      caller will see in the API response rather than a raised exception)
    - bare numeric -> prefixed with 'act_'
    - already 'act_...' -> unchanged
    """
    a = (account_id or "").strip() or DEFAULT_ACCOUNT
    if not a:
        # Surfaces as a Graph 'unknown path' error rather than a tool refusal —
        # consistent with the never-gate contract.
        return "act_MISSING_ACCOUNT_ID"
    return a if a.startswith("act_") else f"act_{a}"

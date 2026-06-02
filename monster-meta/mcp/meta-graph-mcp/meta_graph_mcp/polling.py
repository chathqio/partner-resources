"""Async-job pollers (insights report runs; audience operation_status).

Per rebuild/SCHEMA-VERIFICATION.md §3: fetch async-insights results only when
async_status == "Job Completed" AND async_percent_completion == 100.
"""

import time

from .client import auto_paginate
from .client import request as _request

_DONE = "Job Completed"
_TERMINAL = {"Job Failed", "Job Skipped"}


def poll_insights_report(
    report_run_id: str,
    *,
    max_wait_s: int = 120,
    interval_s: float = 3.0,
    fetch_results: bool = True,
    version: str | None = None,
) -> dict:
    """Poll an AdReportRun until terminal, then (optionally) fetch results.

    Returns {status, percent, report_run_id, data?|error?}.
    """
    waited = 0.0
    status = None
    pct = None
    while waited <= max_wait_s:
        r = _request(
            "GET",
            report_run_id,
            params={"fields": "async_status,async_percent_completion"},
            version=version,
        )
        if not r.get("ok"):
            return {"ok": False, "report_run_id": report_run_id, "error": r.get("error")}
        body = r.get("data") or {}
        status = body.get("async_status")
        pct = body.get("async_percent_completion")
        if status == _DONE and pct == 100:
            if not fetch_results:
                return {"ok": True, "status": status, "percent": pct,
                        "report_run_id": report_run_id}
            res = auto_paginate(
                f"{report_run_id}/insights", limit=100, max_pages=50,
                version=version,
            )
            res.update({"status": status, "percent": pct,
                        "report_run_id": report_run_id})
            return res
        if status in _TERMINAL:
            return {"ok": False, "status": status, "percent": pct,
                    "report_run_id": report_run_id,
                    "error": {"message": f"async report ended: {status}"}}
        time.sleep(interval_s)
        waited += interval_s
    return {"ok": False, "status": status, "percent": pct,
            "report_run_id": report_run_id,
            "error": {"message": f"timeout after {max_wait_s}s (status={status})"}}


def poll_operation_status(
    object_id: str,
    *,
    ready_codes=(200,),
    max_wait_s: int = 120,
    interval_s: float = 3.0,
    version: str | None = None,
) -> dict:
    """Poll a node's operation_status.code (custom/lookalike audience build).
    Returns when code is in ready_codes, terminal-ish (>=400), or on timeout."""
    waited = 0.0
    last = None
    while waited <= max_wait_s:
        r = _request(
            "GET", object_id,
            params={"fields": "operation_status,delivery_status,approximate_count"},
            version=version,
        )
        if not r.get("ok"):
            return {"ok": False, "id": object_id, "error": r.get("error")}
        body = r.get("data") or {}
        last = body
        code = (body.get("operation_status") or {}).get("code")
        if code in ready_codes:
            return {"ok": True, "id": object_id, "status": body}
        if isinstance(code, int) and code >= 400:
            return {"ok": False, "id": object_id, "status": body,
                    "error": {"message": f"operation_status code {code}"}}
        time.sleep(interval_s)
        waited += interval_s
    return {"ok": False, "id": object_id, "status": last,
            "error": {"message": f"timeout after {max_wait_s}s"}}

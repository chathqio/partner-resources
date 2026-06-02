"""Token hygiene: keep the access token out of logs and tool responses."""

import json
import logging
import re

_TOKEN_RE = re.compile(r"access_token=[A-Za-z0-9_\-.|]+")


def silence_http_logging() -> None:
    """httpx/httpcore log full request URLs (incl. ?access_token=...) at INFO.

    Force them to WARNING so the token never reaches stderr / MCP client logs.
    """
    for name in ("httpx", "httpcore", "httpcore.http11", "httpcore.connection"):
        logging.getLogger(name).setLevel(logging.WARNING)


def redact(obj):
    """Strip any access_token=... that slips into a payload (e.g. paging URLs)."""
    s = json.dumps(obj)
    if "access_token=" in s:
        return json.loads(_TOKEN_RE.sub("access_token=<REDACTED>", s))
    return obj

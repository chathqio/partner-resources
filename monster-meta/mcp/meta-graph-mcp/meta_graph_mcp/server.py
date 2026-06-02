"""FastMCP server. Tool modules self-register here.

Primitives guarantee nothing is ever unreachable; the named modules are thin,
additive conveniences (same tool names as the retired third-party meta-ads MCP,
so consumers swap the mcp__meta-ads__ prefix for mcp__meta-graph__ and nothing
else changes).
"""

from mcp.server.fastmcp import FastMCP

from .tools import (
    accounts,
    ads,
    adsets,
    assets,
    audiences,
    business,
    campaigns,
    capi,
    catalogs,
    creatives,
    estimate,
    estimate_extra,
    insights,
    insights_async,
    leadgen,
    misc,
    pixels,
    previews,
    primitives,
    targeting,
    targeting_extra,
)

mcp_server = FastMCP("meta-graph")

# Order: primitives first (the never-refuse guarantee), then named conveniences.
_MODULES = [
    primitives,
    accounts,
    campaigns,
    adsets,
    ads,
    creatives,
    assets,
    insights,
    insights_async,
    targeting,
    targeting_extra,
    estimate,
    estimate_extra,
    audiences,
    capi,
    catalogs,
    leadgen,
    previews,
    pixels,
    business,
    misc,
]

for _m in _MODULES:
    _m.register(mcp_server)


def main() -> None:
    mcp_server.run(transport="stdio")


if __name__ == "__main__":
    main()

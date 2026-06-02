#!/bin/bash
# Launcher for meta-graph-mcp — fully self-contained.
#
# No dependency on tools/meta-ads-mcp. Uses this directory's OWN .venv and
# reads its OWN environment (token, version, default account) injected by the
# MCP client from rev-ops/.mcp.json -> mcpServers.meta-graph.env. No token
# scraping from any other server's config.

set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PY="$HERE/.venv/bin/python"

if [ ! -x "$VENV_PY" ]; then
  echo "meta-graph-mcp: missing venv at $VENV_PY" >&2
  echo "  python3 -m venv \"$HERE/.venv\" && \"$VENV_PY\" -m pip install -r \"$HERE/requirements.txt\"" >&2
  exit 1
fi

# Sane defaults; any value already exported (e.g. from .mcp.json env) wins.
export GRAPH_API_VERSION="${GRAPH_API_VERSION:-v25.0}"
# META_DEFAULT_ACCOUNT intentionally NOT defaulted — the server ships clean for
# the community; set it in .mcp.json env to enable the {account} placeholder.

exec "$VENV_PY" -m meta_graph_mcp

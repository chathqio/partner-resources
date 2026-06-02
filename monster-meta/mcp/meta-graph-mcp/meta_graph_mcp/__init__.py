"""meta-graph-mcp — a comprehensive, self-contained Meta Graph/Marketing API MCP.

Design tenet: this server must NEVER refuse an operation the Graph API supports.
The generic passthrough primitives (graph_get/post/delete/paginate/batch/call)
guarantee every node, edge, field, and API version is reachable; named tools are
thin, additive conveniences layered on top — they never gate.
"""

__version__ = "0.1.0"

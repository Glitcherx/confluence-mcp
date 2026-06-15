"""MCP tools for Confluence search operations."""

import logging
from fastmcp import FastMCP
from confluence.client import ConfluenceClient

logger = logging.getLogger(__name__)

client = ConfluenceClient()


def register_search_tools(mcp: FastMCP):
    """Register all search-related tools with the MCP server."""

    @mcp.tool()
    def search_confluence(query: str, limit: int = 10) -> list[dict]:
        """
        Search Confluence pages using a text query.

        Args:
            query: The text to search for across all Confluence pages
            limit: Maximum number of results to return (default 10)
        """
        logger.info(f"Tool called: search_confluence with query '{query}'")
        results = client.search(query, limit=limit)
        return [
            {
                "id": result.id,
                "title": result.title,
                "space_key": result.space_key,
                "url": result.url,
                "excerpt": result.excerpt,
            }
            for result in results
        ]
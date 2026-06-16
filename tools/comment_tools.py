"""MCP tools for Confluence comment operations."""

import logging
from fastmcp import FastMCP
from confluence.client import ConfluenceClient

logger = logging.getLogger(__name__)

client = ConfluenceClient()


def register_comment_tools(mcp: FastMCP):
    """Register all comment-related tools with the MCP server."""

    @mcp.tool()
    def add_comment(page_id: str, comment: str) -> dict:
        """
        Add a comment to a Confluence page.

        Args:
            page_id: The ID of the page to comment on
            comment: The comment text to add
        """
        logger.info(f"Tool called: add_comment on page {page_id}")
        return client.add_comment(page_id, comment)
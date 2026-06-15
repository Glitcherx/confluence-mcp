"""MCP tools for Confluence page operations."""

import logging
from fastmcp import FastMCP
from confluence.client import ConfluenceClient

logger = logging.getLogger(__name__)

client = ConfluenceClient()


def register_page_tools(mcp: FastMCP):
    """Register all page-related tools with the MCP server."""

    @mcp.tool()
    def get_page(page_id: str) -> dict:
        """
        Get a Confluence page by its ID.

        Args:
            page_id: The unique ID of the Confluence page
        """
        logger.info(f"Tool called: get_page with id {page_id}")
        page = client.get_page(page_id)
        return {
            "id": page.id,
            "title": page.title,
            "space_key": page.space_key,
            "content": page.content,
            "url": page.url,
            "version": page.version,
        }

    @mcp.tool()
    def get_pages_in_space(space_key: str, limit: int = 10) -> list[dict]:
        """
        Get all pages in a Confluence space.

        Args:
            space_key: The key of the space (e.g. 'ENG', 'HR')
            limit: Maximum number of pages to return (default 10)
        """
        logger.info(f"Tool called: get_pages_in_space with key {space_key}")
        pages = client.get_pages_in_space(space_key, limit=limit)
        return [
            {
                "id": page.id,
                "title": page.title,
                "space_key": page.space_key,
                "url": page.url,
                "version": page.version,
            }
            for page in pages
        ]

    @mcp.tool()
    def get_spaces(limit: int = 10) -> list[dict]:
        """
        Get all available Confluence spaces.

        Args:
            limit: Maximum number of spaces to return (default 10)
        """
        logger.info("Tool called: get_spaces")
        spaces = client.get_spaces(limit=limit)
        return [
            {
                "key": space.key,
                "name": space.name,
                "url": space.url,
            }
            for space in spaces
        ]
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
    def create_page(space_key: str, title: str, content: str, parent_id: str = None) -> dict:
        """
        Create a new Confluence page.

        Args:
            space_key: The key of the space to create the page in
            title: The title of the new page
            content: The content of the page in HTML format
            parent_id: Optional ID of the parent page
        """
        logger.info(f"Tool called: create_page '{title}' in {space_key}")
        page = client.create_page(space_key, title, content, parent_id)
        return {
            "id": page.id,
            "title": page.title,
            "space_key": page.space_key,
            "url": page.url,
            "version": page.version,
        }

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
    
    @mcp.tool()
    def get_page_by_title(space_key: str, title: str) -> dict:
        """
        Get a Confluence page by its title and space key.

        Args:
            space_key: The key of the space (e.g. 'ENG', 'SD')
            title: The exact title of the page
        """
        logger.info(f"Tool called: get_page_by_title '{title}' in {space_key}")
        page = client.get_page_by_title(space_key, title)
        return {
            "id": page.id,
            "title": page.title,
            "space_key": page.space_key,
            "content": page.content,
            "url": page.url,
            "version": page.version,
        }
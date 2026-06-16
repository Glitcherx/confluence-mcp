"""Main entry point for the Confluence MCP server."""

from tools.comment_tools import register_comment_tools
import logging
from fastmcp import FastMCP
from tools.page_tools import register_page_tools
from tools.search_tools import register_search_tools

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

# Create the MCP server
mcp = FastMCP(
    name="Confluence MCP",
    instructions="You are a helpful assistant with access to Confluence. "
    "Use the available tools to search and retrieve pages and spaces.",
)

# Register all tools
register_page_tools(mcp)
register_search_tools(mcp)
register_comment_tools(mcp)


if __name__ == "__main__":
    logger.info("Starting Confluence MCP server...")
    mcp.run()
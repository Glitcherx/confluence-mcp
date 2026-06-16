"""Confluence API client."""

import logging
from turtle import title
from atlassian import Confluence
from config import load_config
from confluence.models import Page, Space, SearchResult

logger = logging.getLogger(__name__)


class ConfluenceClient:
    """Client for interacting with Confluence API."""

    def __init__(self):
        """Initialize the Confluence client with config."""
        config = load_config()
        self.client = Confluence(
            url=config.confluence.url,
            username=config.confluence.username,
            password=config.confluence.api_token,
            cloud=True,
        )
        logger.info("Confluence client initialized")

    def get_page(self, page_id: str) -> Page:
        """Get a single page by its ID."""
        logger.info(f"Fetching page {page_id}")
        data = self.client.get_page_by_id(
            page_id,
            expand="body.storage,version"
        )
        return Page(
            id=str(data["id"]),
            title=data["title"],
            space_key=data["space"]["key"],
            content=data["body"]["storage"]["value"],
            url=data["_links"]["webui"],
            version=data["version"]["number"],
        )
    
    def get_page_by_title(self, space_key: str, title: str) -> Page:
        """Get a page by its title and space key."""
        logger.info(f"Fetching page '{title}' in space {space_key}")
        data = self.client.get_page_by_title(
        space=space_key,
        title=title,
        expand="body.storage,version"
        )
        if not data:
            raise ValueError(f"Page '{title}' not found in space '{space_key}'")
        return Page(
        id=str(data["id"]),
        title=data["title"],
        space_key=data["space"]["key"],
        content=data["body"]["storage"]["value"],
        url=data["_links"]["webui"],
        version=data["version"]["number"],
        )
    
    def create_page(self, space_key: str, title: str, content: str, parent_id: str = None) -> Page:
        """Create a new Confluence page."""
        logger.info(f"Creating page '{title}' in space {space_key}")
        data = self.client.create_page(
            space=space_key,
            title=title,
            body=content,
            parent_id=parent_id,
        )
        return Page(
            id=str(data["id"]),
            title=data["title"],
            space_key=data["space"]["key"],
            content=content,
            url=data["_links"]["webui"],
            version=data["version"]["number"],
        )

    def get_pages_in_space(self, space_key: str, limit: int = 10) -> list[Page]:
        """Get multiple pages from a space."""
        logger.info(f"Fetching pages in space {space_key}")
        results = self.client.get_all_pages_from_space(
            space_key,
            limit=limit,
            expand="body.storage,version"
        )
        pages = []
        for data in results:
            pages.append(Page(
                id=str(data["id"]),
                title=data["title"],
                space_key=space_key,
                content=data["body"]["storage"]["value"],
                url=data["_links"]["webui"],
                version=data["version"]["number"],
            ))
        return pages

    def get_spaces(self, limit: int = 10) -> list[Space]:
        """Get all available spaces."""
        logger.info("Fetching spaces")
        data = self.client.get_all_spaces(limit=limit)
        spaces = []
        for item in data["results"]:
            spaces.append(Space(
                key=item["key"],
                name=item["name"],
                url=item["_links"]["webui"],
            ))
        return spaces

    def search(self, query: str, limit: int = 10) -> list[SearchResult]:
        """Search Confluence using CQL."""
        logger.info(f"Searching for: {query}")
        data = self.client.cql(
            f'text ~ "{query}" AND type = page',
            limit=limit,
        )
        results = []
        for item in data["results"]:
            results.append(SearchResult(
                id=str(item["content"]["id"]),
                title=item["content"]["title"],
                space_key=item["resultGlobalContainer"]["title"],
                url=item["content"]["_links"]["webui"],
                excerpt=item.get("excerpt", ""),
            ))
        return results
    
    def add_comment(self, page_id: str, comment: str) -> dict:
        """Add a comment to a Confluence page."""
        logger.info(f"Adding comment to page {page_id}")
        data = self.client.add_comment(page_id, comment)
        return {
            "id": str(data["id"]),
            "page_id": page_id,
            "content": comment,
        }
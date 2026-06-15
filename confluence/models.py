"""Data models for Confluence objects."""

from dataclasses import dataclass


@dataclass
class Space:
    """Represents a Confluence space."""
    key: str
    name: str
    url: str


@dataclass
class Page:
    """Represents a Confluence page."""
    id: str
    title: str
    space_key: str
    content: str
    url: str
    version: int


@dataclass
class SearchResult:
    """Represents a single search result."""
    id: str
    title: str
    space_key: str
    url: str
    excerpt: str
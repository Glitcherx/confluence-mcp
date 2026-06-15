# Confluence MCP Server

A production-ready Model Context Protocol (MCP) server that connects Claude Desktop to Atlassian Confluence, enabling natural language queries against live Confluence data.

## Features

- Search Confluence pages using natural language
- Retrieve pages by ID or space
- List all available Confluence spaces
- Modular, extensible architecture for adding new tools

## Tech Stack

- **Python 3.11**
- **FastMCP** — MCP server framework
- **atlassian-python-api** — Confluence REST API client
- **uv** — Python package manager
- **python-dotenv** — Environment variable management

## Architecture

config.py          # Loads credentials from environment variables
confluence/
models.py        # Data models (Page, Space, SearchResult)
client.py        # Confluence API client
tools/
page_tools.py    # MCP tools for page operations
search_tools.py  # MCP tools for search
server.py          # FastMCP server entry point

## Setup

1. Clone the repository
2. Install dependencies with uv:
```bash
   uv sync
```
3. Create a `.env` file:
CONFLUENCE_URL="https://your-domain.atlassian.net"
CONFLUENCE_USERNAME="your-email@example.com"
CONFLUENCE_PAT="your-api-token"
4. Add to Claude Desktop config and restart

## Available Tools

| Tool | Description |
|------|-------------|
| `get_page` | Retrieve a Confluence page by ID |
| `get_pages_in_space` | List all pages in a space |
| `get_spaces` | List all available spaces |
| `search_confluence` | Search pages by text query |

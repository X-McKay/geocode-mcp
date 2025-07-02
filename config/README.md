# Configuration Files

This directory contains configuration files for integrating the Geocode MCP Server with different tools and editors.

## Files

### MCP Server Configurations
- **`cursor-mcp.json`** - Cursor editor MCP configuration
- **`vscode-mcp.json`** - VS Code MCP configuration  
- **`claude-desktop.json`** - Claude Desktop MCP configuration

## Usage

All configurations use the same pattern - they install and run the `geocode-mcp` package via `uvx`:

### Cursor
Copy the contents of `cursor-mcp.json` to your Cursor MCP configuration:

```json
{
  "mcpServers": {
    "geocoding": {
      "command": "uvx",
      "args": ["geocode-mcp"]
    }
  }
}
```

### VS Code
Copy the contents of `vscode-mcp.json` to your VS Code MCP configuration:

```json
{
  "mcpServers": {
    "geocoding": {
      "command": "uvx",
      "args": ["geocode-mcp"]
    }
  }
}
```

### Claude Desktop
Copy the contents of `claude-desktop.json` to your Claude Desktop configuration file (usually located at `~/.config/claude-desktop/config.json` on Linux/Mac or `%APPDATA%\Claude\config.json` on Windows):

```json
{
  "mcpServers": {
    "geocoding": {
      "command": "uvx",
      "args": ["geocode-mcp"]
    }
  }
}
```

## Prerequisites

Before using any of these configurations, make sure you have:

1. **uvx installed**: `pip install uvx` or `pipx install uvx`
2. **The package published**: The `geocode-mcp` package needs to be available on PyPI

## Local Development

For local development (before publishing), you can use:

```json
{
  "mcpServers": {
    "geocoding": {
      "command": "python",
      "args": ["-m", "geocode_mcp.server"],
      "cwd": "/path/to/geocode-mcp",
      "env": {
        "PYTHONPATH": "/path/to/geocode-mcp/src"
      }
    }
  }
}
```

## Available Tools

Once configured, the MCP server provides:

- **`mcp_geocoding_get_coordinates`**: Get latitude/longitude coordinates for any location
  - Parameters: `location` (required), `limit` (optional, max 10)
  - Uses OpenStreetMap Nominatim API (free, no API key required) 
# Cursor MCP Integration Guide

This guide explains how to integrate the Geocoding MCP Server with Cursor.

## Quick Setup (Recommended)

### 1. Install the Package
The easiest way is to use the published package:

```bash
uvx geocode-mcp
```

### 2. Configure in Cursor

Add this configuration to your Cursor MCP settings:

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

You can copy this exact configuration from [`config/cursor-mcp.json`](../config/cursor-mcp.json).

## Development Setup

If you're developing or testing locally:

### 1. Install Development Dependencies
```bash
# Clone and install
git clone https://github.com/X-McKay/geocode-mcp.git
cd geocode-mcp
pip install -e ".[dev]"
```

### 2. Test the Server
```bash
pytest tests/test_mcp_server.py -v
```

### 3. Configure for Local Development

Use this configuration for local development:

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

Once integrated, you can use this tool in Cursor:

### `mcp_geocoding_get_coordinates`
Get latitude and longitude coordinates for a city or location.

**Parameters:**
- `location` (required): City name, address, or location (e.g., 'New York', 'Paris, France', '123 Main St, Seattle')
- `limit` (optional): Maximum number of results to return (default: 1, max: 10)

**Example Usage:**
```
Get coordinates for Tokyo, Japan
Find the latitude and longitude of London, UK
What are the coordinates for New York City?
Get coordinates for "1600 Pennsylvania Avenue, Washington DC" with limit 3
```

**Response includes:**
- Latitude and longitude
- Display name of the location
- Place ID from OpenStreetMap
- Location type and classification
- Importance ranking
- Bounding box coordinates

## Configuration Methods

### Method 1: Cursor Settings UI
1. Open Cursor Settings (`Ctrl+,` or `Cmd+,`)
2. Search for "MCP" 
3. Add the geocoding server configuration

### Method 2: Settings JSON
1. Open Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
2. Type "Preferences: Open Settings (JSON)"
3. Add the MCP server configuration to your settings

### Method 3: Workspace Configuration
Add the configuration to your workspace's `.cursor/settings.json` file.

## Testing the Integration

1. **Restart Cursor** after adding the MCP server configuration
2. **Open a chat** in Cursor  
3. **Try these example prompts:**
   - "What are the coordinates for Paris, France?"
   - "Get the latitude and longitude of Tokyo"
   - "Find coordinates for Seattle, Washington"
   - "Get coordinates for multiple results: London with limit 3"

## Troubleshooting

### Server Won't Start
- **Check uvx installation**: `uvx --version`
- **Verify package availability**: `uvx geocode-mcp --help`
- **Check package installation**: `pip show geocode-mcp`

### Tools Not Available in Cursor
- **Restart Cursor** completely after configuration changes
- **Check MCP server status** in Cursor's developer tools/logs
- **Verify configuration syntax** - JSON must be valid
- **Test locally**: `python -m geocode_mcp.server` (for development setup)

### Permission Issues
- On some systems, you may need to adjust file permissions
- Try running: `chmod +x $(which geocode-mcp)` if using pip installation

### Development Issues
- **Install in development mode**: `pip install -e ".[dev]"`
- **Run tests**: `pytest tests/ -v`
- **Check Python path**: Ensure `src/` is in PYTHONPATH for local development

## Getting Help

- Check the [main README](../README.md) for general usage
- Review [configuration examples](../config/) for other tools
- Open an issue on [GitHub](https://github.com/X-McKay/geocode-mcp/issues) if you encounter problems
 
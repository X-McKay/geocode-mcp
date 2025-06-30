# Cursor MCP Integration Guide

This guide explains how to integrate the Geocoding MCP Server with Cursor.

## Quick Setup

### 1. Install Dependencies
```bash
make install-dev
```

### 2. Test the Server
```bash
python tests/test_mcp_server.py
```

### 3. Configure in Cursor

#### Option A: Using Cursor Settings UI
1. Open Cursor Settings (`Ctrl+,`)
2. Search for "MCP" or "Model Context Protocol"
3. Add a new MCP server with these settings:
   ```json
   {
     "name": "geocoding",
     "command": "python",
     "args": ["/path/to/geocode-mcp/scripts/run_mcp_server.py"],
     "cwd": "/path/to/geocode-mcp"
   }
   ```

#### Option B: Using Settings JSON
1. Open Settings JSON (`Ctrl+Shift+P` → "Preferences: Open Settings (JSON)")
2. Add this configuration:
   ```json
   {
     "mcp.servers": {
       "geocoding": {
         "command": "python",
         "args": ["/path/to/geocode-mcp/scripts/run_mcp_server.py"],
         "cwd": "/path/to/geocode-mcp"
       }
     }
   }
   ```

#### Option C: Using Configuration File
You can also reference the example configuration in `config/cursor-mcp.json`:
```json
{
  "mcpServers": {
    "geocoding": {
      "command": "python",
      "args": ["-m", "geocode.mcp_server"],
      "env": {
        "PYTHONPATH": "${workspaceFolder}/src"
      }
    }
  }
}
```

## Available Tools

Once integrated, you can use these tools in Cursor:

### `get_coordinates`
Get latitude and longitude coordinates for a city or location.

**Parameters:**
- `location` (required): City name, address, or location (e.g., 'New York', 'Paris, France')
- `limit` (optional): Maximum number of results (default: 1, max: 10)

**Example Usage:**
```
Get coordinates for Tokyo, Japan
Find the latitude and longitude of London, UK
What are the coordinates for New York City?
```

## Testing the Integration

1. **Restart Cursor** after adding the MCP server
2. **Open a chat** in Cursor
3. **Try these prompts:**
   - "What are the coordinates for Paris, France?"
   - "Get the latitude and longitude of Tokyo"
   - "Find coordinates for multiple cities: London, Berlin, and Rome"

## Troubleshooting

### Server Won't Start
- Ensure all dependencies are installed: `make install-dev`
- Check Python path: `python scripts/run_mcp_server.py`
- Verify the server script is executable: `chmod +x scripts/run_mcp_server.py`

### Tools Not Available
- Restart Cursor after configuration
- Check Cursor's MCP logs for errors
- Verify the server is running: `python tests/test_mcp_server.py`

### Permission Issues
- Make sure the script paths are absolute
- Check file permissions on the Python script
- Ensure the working directory is correct

## Development

### Running Tests
```bash
make test
```

### Linting and Formatting
```bash
make lint
make format
```

### Type Checking
```bash
make type-check
```

### All Checks
```bash
make check-all
```

## File Organization

The project is organized as follows:
- **`src/geocode/`** - Main source code
- **`tests/`** - All test files
- **`scripts/`** - Executable scripts
- **`config/`** - Configuration files
- **`docs/`** - Documentation 
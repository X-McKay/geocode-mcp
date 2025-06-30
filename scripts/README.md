# Scripts

This directory contains executable scripts for running the MCP server and other utilities.

## Files

### MCP Server Scripts
- **`run_mcp_server.py`** - Standalone script to run the MCP server

## Usage

### Running the MCP Server
```bash
# From the project root
python scripts/run_mcp_server.py

# Or make it executable and run directly
chmod +x scripts/run_mcp_server.py
./scripts/run_mcp_server.py
```

### For Cursor Integration
Use this script path in your Cursor MCP configuration:
```json
{
  "command": "python",
  "args": ["/path/to/geocode-mcp/scripts/run_mcp_server.py"],
  "cwd": "/path/to/geocode-mcp"
}
```

## Adding New Scripts

When adding new scripts:
1. Make them executable: `chmod +x scripts/script_name.py`
2. Add shebang line: `#!/usr/bin/env python3`
3. Include proper error handling
4. Add usage documentation
5. Update this README 
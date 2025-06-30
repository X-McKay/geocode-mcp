# Configuration Files

This directory contains configuration files for different integrations and environments.

## Files

### MCP Server Configurations
- **`cursor-mcp.json`** - Cursor MCP server configuration example

## Usage

### Cursor Integration
Use `cursor-mcp.json` as a reference when configuring the MCP server in Cursor:

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

## Adding New Configurations

When adding new configuration files:
1. Use descriptive names (e.g., `vscode-mcp.json`, `neovim-mcp.json`)
2. Include a comment explaining the configuration
3. Update this README with usage instructions
4. Test the configuration before committing 
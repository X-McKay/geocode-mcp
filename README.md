# Geocode MCP Server

A Model Context Protocol (MCP) server for producing latitude/longitude coordinates for cities and areas using the OpenStreetMap Nominatim API.

## Features

- 🌍 **Geocoding**: Get coordinates for any location worldwide
- 🆓 **Free API**: Uses OpenStreetMap Nominatim (no API key required)
- 🛠️ **MCP Integration**: Works with Cursor, VSCode, and other MCP-compatible editors
- 🧪 **Comprehensive Testing**: Full test suite with unit and integration tests
- 📦 **Modern Tooling**: Ruff for linting, ty for type checking, pytest for testing

## Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd geocode-mcp

# Install dependencies
make install-dev
```

### Running the Server

```bash
# Run the MCP server
python scripts/run_mcp_server.py

# Or make it executable and run directly
chmod +x scripts/run_mcp_server.py
./scripts/run_mcp_server.py
```

### Testing

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test files
pytest tests/test_geocoding.py -v
python tests/test_mcp_server.py
```

## Integration Guides

- **[Cursor Integration](docs/cursor-integration.md)** - How to integrate with Cursor
- **[VSCode Integration](tests/test_vscode.py)** - VSCode integration tests and setup

## Project Structure

```
geocode-mcp/
├── src/geocode/           # Main source code
│   └── mcp_server.py     # MCP server implementation
├── tests/                 # All test files
│   ├── test_geocoding.py # Unit tests for geocoding
│   ├── test_mcp.py       # Unit tests for MCP server
│   ├── test_mcp_server.py # Integration tests
│   └── test_vscode.py    # VSCode integration tests
├── scripts/              # Executable scripts
│   └── run_mcp_server.py # MCP server runner
├── config/               # Configuration files
│   └── cursor-mcp.json   # Cursor MCP configuration
├── docs/                 # Documentation
│   └── cursor-integration.md
├── Makefile              # Development commands
├── pyproject.toml        # Project configuration
└── README.md            # This file
```

## Available Tools

### `get_coordinates`
Get latitude and longitude coordinates for a city or location.

**Parameters:**
- `location` (required): City name, address, or location
- `limit` (optional): Maximum number of results (default: 1, max: 10)

**Example Usage:**
```
Get coordinates for Tokyo, Japan
Find the latitude and longitude of London, UK
What are the coordinates for New York City?
```

## Development

### Code Quality

```bash
# Lint code
make lint

# Format code
make format

# Type check
make type-check

# Run all checks
make check-all
```

### Testing

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test categories
pytest tests/test_geocoding.py -v  # Geocoding tests
pytest tests/test_mcp.py -v        # MCP server tests
python tests/test_mcp_server.py    # Integration tests
python tests/test_vscode.py        # VSCode tests
```

### Installation

```bash
# Install production dependencies
make install

# Install development dependencies
make install-dev
```

## Configuration

### Cursor Integration
See [Cursor Integration Guide](docs/cursor-integration.md) for detailed setup instructions.

### VSCode Integration
Run the VSCode integration tests:
```bash
python tests/test_vscode.py
```

## API Reference

### Geocoding Function
```python
async def geocode_location(location: str, limit: int = 1) -> dict[str, Any]:
    """Geocode a location using Nominatim API."""
```

### MCP Server
The server provides the `get_coordinates` tool that can be called via the MCP protocol.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `make test`
5. Run linting: `make lint`
6. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenStreetMap](https://www.openstreetmap.org/) for providing the Nominatim geocoding service
- [MCP](https://modelcontextprotocol.io/) for the protocol specification
```

---

## 🚀 Quick Setup Instructions

1. **Create Project Folder:**
   ```bash
   mkdir mcp-geocoding-server-python
   cd mcp-geocoding-server-python
   ```

2. **Copy Files:** 
   Copy each file section above into files with the respective names

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Server:**
   ```bash
   python geocoding_server.py
   ```

5. **Configure MCP Client:**
   Add to your MCP client (like Claude Desktop) configuration:
   ```json
   {
     "mcpServers": {
       "geocoding": {
         "command": "python",
         "args": ["/full/path/to/mcp-geocoding-server-python/geocoding_server.py"]
       }
     }
   }
# Geocode MCP Server

A Model Context Protocol (MCP) server that provides latitude/longitude coordinates for cities and locations using the OpenStreetMap Nominatim API.

## Features

- 🌍 **Global Geocoding**: Get coordinates for any location worldwide
- 🆓 **Free API**: Uses OpenStreetMap Nominatim (no API key required)
- � **MCP Integration**: Works with Cursor, VS Code, Claude Desktop, and other MCP-compatible tools
- 📦 **Easy Installation**: Install via PyPI with `uvx geocode-mcp`
- �️ **Modern Tooling**: Built with Python 3.12+, async/await, and comprehensive testing

## Quick Start

### Installation

Install the package from PyPI using uvx (recommended):

```bash
uvx geocode-mcp
```

Or install with pip:

```bash
pip install geocode-mcp
```

### MCP Configuration

Add to your MCP client configuration:

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

See the [`config/`](config/) directory for specific examples for different tools.

## Available Tools

### `mcp_geocoding_get_coordinates`

Get latitude and longitude coordinates for a city or location.

**Parameters:**
- `location` (required): City name, address, or location (e.g., "New York", "Paris, France", "123 Main St, Seattle")
- `limit` (optional): Maximum number of results to return (default: 1, max: 10)

**Example Usage:**
```
Get coordinates for Tokyo, Japan
Find the latitude and longitude of London, UK  
What are the coordinates for New York City?
Get coordinates for "1600 Pennsylvania Avenue, Washington DC" with limit 5
```

**Response Format:**
```json
{
  "query": "Tokyo, Japan",
  "results_count": 1,
  "coordinates": [
    {
      "latitude": 35.6762,
      "longitude": 139.6503,
      "display_name": "Tokyo, Japan",
      "place_id": "282885117",
      "type": "city",
      "class": "place",
      "importance": 0.9,
      "bounding_box": {
        "south": 35.619,
        "north": 35.739,
        "west": 139.619,
        "east": 139.682
      }
    }
  ]
}
```

## Integration Guides

### Cursor
Copy the configuration from [`config/cursor-mcp.json`](config/cursor-mcp.json) to your Cursor MCP settings.

### VS Code  
Copy the configuration from [`config/vscode-mcp.json`](config/vscode-mcp.json) to your VS Code MCP settings.

### Claude Desktop
Copy the configuration from [`config/claude-desktop.json`](config/claude-desktop.json) to your Claude Desktop config file.

See the [config README](config/README.md) for detailed setup instructions.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/X-McKay/geocode-mcp.git
cd geocode-mcp

# Install with development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/geocode_mcp --cov-report=html

# Run specific test files
pytest tests/test_geocoding.py -v
pytest tests/test_mcp_server.py -v
```

### Code Quality

```bash
# Format code
ruff format

# Lint code
ruff check

# Run all checks
ruff check && ruff format --check
```

### Local Development

For local development and testing, you can run the server directly:

```bash
python -m geocode_mcp.server
```

Or use the development configuration in your MCP client:

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

## Project Structure

```
geocode-mcp/
├── src/geocode_mcp/       # Main source code
│   └── server.py          # MCP server implementation
├── tests/                 # Test suite
│   ├── test_geocoding.py  # Geocoding functionality tests
│   ├── test_mcp_server.py # MCP server integration tests
│   ├── test_mcp.py        # MCP protocol tests
│   └── test_vscode.py     # VS Code integration tests
├── config/                # Configuration examples
│   ├── cursor-mcp.json    # Cursor configuration
│   ├── vscode-mcp.json    # VS Code configuration
│   ├── claude-desktop.json # Claude Desktop configuration
│   └── README.md          # Configuration guide
├── docs/                  # Documentation
├── pyproject.toml         # Project configuration
├── requirements.txt       # Production dependencies
├── requirements-dev.txt   # Development dependencies
└── README.md             # This file
```

## API Reference

### Core Functions

```python
async def geocode_location(location: str, limit: int = 1) -> dict[str, Any]:
    """
    Geocode a location using OpenStreetMap Nominatim API.
    
    Args:
        location: The location to geocode
        limit: Maximum number of results (1-10)
        
    Returns:
        Dictionary containing query, results_count, and coordinates
    """
```

### MCP Server

The server implements the Model Context Protocol and provides the `mcp_geocoding_get_coordinates` tool for use in MCP-compatible applications.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Run linting (`ruff check && ruff format`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenStreetMap](https://www.openstreetmap.org/) for providing the free Nominatim geocoding service
- [Model Context Protocol](https://modelcontextprotocol.io/) for the protocol specification
- The Python MCP SDK team for the excellent tooling
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
# MCP Geocoding Tool (Python)

A Model Context Protocol (MCP) server that provides geocoding functionality to convert city names and locations into latitude and longitude coordinates. Uses the free OpenStreetMap Nominatim API, so no API keys are required.

## Features

- Convert city names, addresses, and locations to lat/lng coordinates
- Support for multiple result limits (1-10 results)
- Detailed location information including bounding boxes
- No API key required (uses OpenStreetMap Nominatim)
- Error handling with helpful suggestions
- Pure Python implementation with async support

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Extract the zip file and navigate to the directory:
```bash
cd mcp-geocoding-server-python
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install mcp aiohttp
```

### Alternative: Install as Package

```bash
pip install -e .
```

## Usage

### Running the Server

Direct execution:
```bash
python geocoding_server.py
```

Or if installed as a package:
```bash
mcp-geocoding-server
```

### Configuring with MCP Clients

Add this server to your MCP client configuration. For example, in Claude Desktop's configuration:

```json
{
  "mcpServers": {
    "geocoding": {
      "command": "python",
      "args": ["/path/to/your/mcp-geocoding-server-python/geocoding_server.py"]
    }
  }
}
```

Or if installed as a package:

```json
{
  "mcpServers": {
    "geocoding": {
      "command": "mcp-geocoding-server"
    }
  }
}
```

### Available Tools

#### `get_coordinates`

Gets latitude and longitude coordinates for a given location.

**Parameters:**
- `location` (string, required): City name, address, or location description
- `limit` (number, optional): Maximum number of results to return (1-10, default: 1)

**Example Usage:**

```python
# Simple city lookup
get_coordinates({
    "location": "New York"
})

# More specific location
get_coordinates({
    "location": "Paris, France"
})

# Address lookup
get_coordinates({
    "location": "123 Main Street, Seattle, WA"
})

# Multiple results
get_coordinates({
    "location": "Springfield",
    "limit": 5
})
```

**Example Response:**

```json
{
  "query": "New York",
  "results_count": 1,
  "coordinates": [
    {
      "latitude": 40.7127281,
      "longitude": -74.0060152,
      "display_name": "New York, United States",
      "place_id": 298085,
      "type": "city",
      "class": "place",
      "importance": 0.9756419939577,
      "bounding_box": {
        "south": 40.4960439,
        "north": 40.9152414,
        "west": -74.2557349,
        "east": -73.7000091
      }
    }
  ]
}
```

### Error Handling

The tool provides helpful error messages and suggestions when locations cannot be found:

```json
{
  "error": "No coordinates found for the specified location",
  "query": "Nonexistent Place",
  "suggestions": [
    "Try including more specific details (e.g., state, country)",
    "Check spelling of the location name",
    "Use a more general location (e.g., city instead of specific address)"
  ]
}
```

## Development

### Project Structure

```
mcp-geocoding-server-python/
├── geocoding_server.py    # Main MCP server implementation
├── requirements.txt       # Python dependencies
├── setup.py              # Package configuration
└── README.md             # This file
```

### Running in Development Mode

```bash
# Install in development mode
pip install -e .

# Run the server
python geocoding_server.py
```

## API Details

This tool uses the OpenStreetMap Nominatim API:
- **Service**: https://nominatim.openstreetmap.org/
- **Rate Limits**: Please be respectful of the free service
- **Attribution**: Data © OpenStreetMap contributors

## Dependencies

- **mcp**: Model Context Protocol SDK for Python
- **aiohttp**: Async HTTP client for making API requests

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to use this in your own projects.

## Notes

- The tool includes a proper User-Agent header as required by Nominatim
- Network errors are handled gracefully with async/await
- Results include detailed information beyond just coordinates
- Bounding boxes are provided for spatial applications
- The importance score can help rank multiple results
- Async implementation for better performance

## Troubleshooting

**"Network error: Unable to connect to geocoding service"**
- Check your internet connection
- Verify that nominatim.openstreetmap.org is accessible
- Try again in a few moments (rate limiting)

**"No coordinates found for the specified location"**
- Check the spelling of your location
- Try adding more specific details (state, country)
- Use a more general location name

**MCP Connection Issues**
- Ensure Python 3.8+ is installed
- Check that all dependencies are installed (`pip install -r requirements.txt`)
- Verify the path in your MCP client config is correct
- Try running the script directly to test for errors

**Import Errors**
- Make sure you have the `mcp` package installed: `pip install mcp`
- Install aiohttp: `pip install aiohttp`
- Check your Python version: `python --version` (should be 3.8+)
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
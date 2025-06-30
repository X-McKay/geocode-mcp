#!/usr/bin/env python3

"""
MCP Geocoding Server
Provides latitude and longitude coordinates for cities/locations
Uses OpenStreetMap Nominatim API (free, no API key required)
"""

import asyncio
import json
from typing import Any, Dict, List, Optional, Sequence
import aiohttp
from urllib.parse import quote

from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types
from mcp.server import NotificationOptions, Server


# Global HTTP session
http_session: Optional[aiohttp.ClientSession] = None

# Create the server instance
server = Server("geocoding-server")


async def get_http_session() -> aiohttp.ClientSession:
    """Get or create the global HTTP session."""
    global http_session
    if http_session is None:
        http_session = aiohttp.ClientSession()
    return http_session


async def close_http_session():
    """Close the global HTTP session."""
    global http_session
    if http_session:
        await http_session.close()
        http_session = None


async def geocode_location(location: str, limit: int = 1) -> Dict[str, Any]:
    """Geocode a location using Nominatim API."""
    session = await get_http_session()
    
    encoded_location = quote(location)
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={encoded_location}&limit={limit}&addressdetails=1"

    headers = {
        'User-Agent': 'MCP-Geocoding-Tool/1.0 (Python)'
    }

    try:
        async with session.get(url, headers=headers) as response:
            if not response.ok:
                raise Exception(f"Nominatim API error: {response.status} {response.reason}")

            data = await response.json()

            if not data:
                return {
                    "error": "No coordinates found for the specified location",
                    "query": location,
                    "suggestions": [
                        "Try including more specific details (e.g., state, country)",
                        "Check spelling of the location name",
                        "Use a more general location (e.g., city instead of specific address)"
                    ]
                }

            results = []
            for item in data:
                result = {
                    "latitude": float(item["lat"]),
                    "longitude": float(item["lon"]),
                    "display_name": item["display_name"],
                    "place_id": item["place_id"],
                    "type": item.get("type", ""),
                    "class": item.get("class", ""),
                    "importance": item.get("importance", 0),
                    "bounding_box": {
                        "south": float(item["boundingbox"][0]),
                        "north": float(item["boundingbox"][1]),
                        "west": float(item["boundingbox"][2]),
                        "east": float(item["boundingbox"][3])
                    }
                }
                results.append(result)

            return {
                "query": location,
                "results_count": len(results),
                "coordinates": results
            }

    except aiohttp.ClientError as error:
        raise Exception(f"Network error: Unable to connect to geocoding service - {str(error)}")


@server.list_tools()
async def handle_list_tools() -> List[types.Tool]:
    """List available tools."""
    return [
        types.Tool(
            name="get_coordinates",
            description="Get latitude and longitude coordinates for a city or location",
            inputSchema={
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name, address, or location (e.g., 'New York', 'Paris, France', '123 Main St, Seattle')",
                    },
                    "limit": {
                        "type": "number",
                        "description": "Maximum number of results to return (default: 1, max: 10)",
                        "default": 1,
                        "minimum": 1,
                        "maximum": 10,
                    },
                },
                "required": ["location"],
            },
        )
    ]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict[str, Any]
) -> Sequence[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Handle tool calls."""
    if name == "get_coordinates":
        try:
            location = arguments.get("location", "").strip()
            limit = min(int(arguments.get("limit", 1)), 10)

            if not location:
                raise ValueError("Location parameter is required and cannot be empty")

            coordinates = await geocode_location(location, limit)
            
            return [
                types.TextContent(
                    type="text", 
                    text=json.dumps(coordinates, indent=2)
                )
            ]
        except Exception as error:
            return [
                types.TextContent(
                    type="text",
                    text=f"Error: {str(error)}"
                )
            ]
    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    """Main entry point for the server."""
    # Initialize options
    options = InitializationOptions(
        server_name="geocoding-server",
        server_version="0.1.0",
        capabilities=server.get_capabilities(
            notification_options=NotificationOptions(),
            experimental_capabilities={},
        ),
    )
    
    try:
        async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                options,
            )
    finally:
        await close_http_session()


if __name__ == "__main__":
    asyncio.run(main())
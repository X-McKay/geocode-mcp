#!/usr/bin/env python3

"""
Comprehensive tests for the MCP Geocoding Server
"""

import json
import os
import sys
from unittest.mock import AsyncMock, patch

import pytest  # type: ignore

# Add the parent directory to the path so we can import the server
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from geocode_mcp.server import geocode_location, handle_call_tool, handle_list_tools


class TestGeocodingServer:
    """Test cases for the geocoding server functionality."""

    @pytest.mark.asyncio
    async def test_geocode_location_success(self):
        """Test successful geocoding with mocked HTTP response."""
        mock_response_data = [
            {
                "lat": "40.7127281",
                "lon": "-74.0060152",
                "display_name": "New York, United States",
                "place_id": 298085,
                "type": "city",
                "class": "place",
                "importance": 0.9756419939577,
                "boundingbox": [
                    "40.4960439",
                    "40.9152414",
                    "-74.2557349",
                    "-73.7000091",
                ],
            }
        ]

        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_response = AsyncMock()
            mock_response.ok = True
            mock_response.json = AsyncMock(return_value=mock_response_data)
            mock_get.return_value.__aenter__.return_value = mock_response

            result = await geocode_location("New York")

            assert result["query"] == "New York"
            assert result["results_count"] == 1
            assert len(result["coordinates"]) == 1
            assert result["coordinates"][0]["latitude"] == 40.7127281
            assert result["coordinates"][0]["longitude"] == -74.0060152

    @pytest.mark.asyncio
    async def test_geocode_location_not_found(self):
        """Test geocoding when no results are found."""
        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_response = AsyncMock()
            mock_response.ok = True
            mock_response.json = AsyncMock(return_value=[])
            mock_get.return_value.__aenter__.return_value = mock_response

            result = await geocode_location("NonexistentPlace12345")

            assert "error" in result
            assert result["query"] == "NonexistentPlace12345"
            assert "suggestions" in result

    @pytest.mark.asyncio
    async def test_geocode_location_multiple_results(self):
        """Test geocoding with multiple results."""
        mock_response_data = [
            {
                "lat": "39.7817213",
                "lon": "-89.6501481",
                "display_name": "Springfield, Illinois, United States",
                "place_id": 123,
                "type": "city",
                "class": "place",
                "importance": 0.8,
                "boundingbox": ["39.7", "39.8", "-89.7", "-89.6"],
            },
            {
                "lat": "42.1014831",
                "lon": "-72.589811",
                "display_name": "Springfield, Massachusetts, United States",
                "place_id": 456,
                "type": "city",
                "class": "place",
                "importance": 0.7,
                "boundingbox": ["42.0", "42.1", "-72.6", "-72.5"],
            },
        ]

        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_response = AsyncMock()
            mock_response.ok = True
            mock_response.json = AsyncMock(return_value=mock_response_data)
            mock_get.return_value.__aenter__.return_value = mock_response

            result = await geocode_location("Springfield", limit=2)

            assert result["results_count"] == 2
            assert len(result["coordinates"]) == 2

    @pytest.mark.asyncio
    async def test_geocode_location_network_error(self):
        """Test geocoding with network error."""
        import aiohttp

        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_get.side_effect = aiohttp.ClientError("Connection failed")

            with pytest.raises(Exception) as exc_info:
                await geocode_location("New York")

            assert "Network error" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_geocode_location_api_error(self):
        """Test geocoding with API error response."""
        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_response = AsyncMock()
            mock_response.ok = False
            mock_response.status = 500
            mock_response.reason = "Internal Server Error"
            mock_get.return_value.__aenter__.return_value = mock_response

            with pytest.raises(Exception) as exc_info:
                await geocode_location("New York")

            assert "Nominatim API error" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_list_tools(self):
        """Test that the server lists available tools correctly."""
        tools = await handle_list_tools()
        assert len(tools) == 1
        assert tools[0].name == "get_coordinates"
        assert "latitude and longitude" in tools[0].description.lower()
        assert "location" in tools[0].inputSchema["properties"]
        assert "limit" in tools[0].inputSchema["properties"]

    @pytest.mark.asyncio
    async def test_call_tool_success(self):
        """Test successful tool call."""
        mock_response_data = [
            {
                "lat": "48.8566969",
                "lon": "2.3514616",
                "display_name": "Paris, France",
                "place_id": 789,
                "type": "city",
                "class": "place",
                "importance": 0.9,
                "boundingbox": ["48.8", "48.9", "2.3", "2.4"],
            }
        ]
        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_response = AsyncMock()
            mock_response.ok = True
            mock_response.json = AsyncMock(return_value=mock_response_data)
            mock_get.return_value.__aenter__.return_value = mock_response
            result = await handle_call_tool(
                "get_coordinates", {"location": "Paris, France"}
            )
            assert len(result) == 1
            response_data = json.loads(result[0].text)
            assert response_data["query"] == "Paris, France"
            assert response_data["results_count"] == 1

    @pytest.mark.asyncio
    async def test_call_tool_invalid_tool(self):
        """Test calling an invalid tool."""
        with pytest.raises(ValueError) as exc_info:
            await handle_call_tool("invalid_tool", {"location": "Paris"})
        assert "Unknown tool" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_call_tool_missing_location(self):
        """Test calling tool without required location parameter."""
        result = await handle_call_tool("get_coordinates", {})
        assert len(result) == 1
        assert "Error:" in result[0].text
        assert "required" in result[0].text.lower()

    @pytest.mark.asyncio
    async def test_call_tool_empty_location(self):
        """Test calling tool with empty location parameter."""
        result = await handle_call_tool("get_coordinates", {"location": ""})
        assert len(result) == 1
        assert "Error:" in result[0].text
        assert "cannot be empty" in result[0].text.lower()

    @pytest.mark.asyncio
    async def test_call_tool_with_limit(self):
        """Test calling tool with limit parameter."""
        mock_response_data = [
            {
                "lat": "40.7127281",
                "lon": "-74.0060152",
                "display_name": "New York, United States",
                "place_id": 298085,
                "type": "city",
                "class": "place",
                "importance": 0.9756419939577,
                "boundingbox": [
                    "40.4960439",
                    "40.9152414",
                    "-74.2557349",
                    "-73.7000091",
                ],
            }
        ]
        with patch("aiohttp.ClientSession.get") as mock_get:
            mock_response = AsyncMock()
            mock_response.ok = True
            mock_response.json = AsyncMock(return_value=mock_response_data)
            mock_get.return_value.__aenter__.return_value = mock_response
            result = await handle_call_tool(
                "get_coordinates", {"location": "New York", "limit": 5}
            )
            assert len(result) == 1
            response_data = json.loads(result[0].text)
            assert response_data["query"] == "New York"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

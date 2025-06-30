#!/usr/bin/env python3
"""
Standalone MCP Geocoding Server Runner
Run this script to start the MCP server for Cursor integration
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from geocode_mcp.server import run_server

if __name__ == "__main__":
    run_server() 
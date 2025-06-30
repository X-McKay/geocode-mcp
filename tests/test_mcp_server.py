#!/usr/bin/env python3
"""
Test script for the MCP Geocoding Server
"""

import asyncio
import json
import os
import subprocess
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))


async def test_mcp_server():
    """Test the MCP server with proper initialization."""

    # Start the server process
    process = subprocess.Popen(
        [
            sys.executable,
            os.path.join(
                os.path.dirname(__file__), "..", "scripts", "run_mcp_server.py"
            ),
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=os.path.dirname(os.path.dirname(__file__)),
    )

    try:
        # Send initialization request
        init_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test-client", "version": "1.0.0"},
            },
        }

        # Send init request
        init_json = json.dumps(init_request) + "\n"
        stdout, stderr = process.communicate(input=init_json, timeout=5)

        print("Server response:")
        print(stdout)
        if stderr:
            print("Stderr:", stderr)

    except subprocess.TimeoutExpired:
        print("Server timed out")
        process.kill()
    except Exception as e:
        print(f"Error: {e}")
        process.kill()


if __name__ == "__main__":
    asyncio.run(test_mcp_server())

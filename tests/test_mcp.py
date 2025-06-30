#!/usr/bin/env python3

"""
Test script to verify MCP server functionality
This simulates MCP client requests to test the server
"""

import asyncio
import json
import subprocess
import sys
from typing import Dict, Any

class MCPTester:
    def __init__(self, server_path: str):
        self.server_path = server_path
        self.process = None
        
    async def send_mcp_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Send a request to the MCP server and get response."""
        
        # Convert request to JSON-RPC format
        jsonrpc_request = {
            "jsonrpc": "2.0",
            "id": 1,
            **request
        }
        
        request_str = json.dumps(jsonrpc_request) + "\n"
        
        # Start the server process
        self.process = subprocess.Popen(
            [sys.executable, self.server_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        try:
            # Send request and get response
            stdout, stderr = self.process.communicate(input=request_str, timeout=10)
            
            if stderr:
                print(f"⚠️  Server stderr: {stderr}")
            
            # Parse response
            lines = stdout.strip().split('\n')
            for line in lines:
                if line.strip():
                    try:
                        return json.loads(line)
                    except json.JSONDecodeError:
                        continue
                        
            return {"error": "No valid JSON response received"}
            
        except subprocess.TimeoutExpired:
            self.process.kill()
            return {"error": "Server request timed out"}
        except Exception as e:
            return {"error": f"Communication error: {str(e)}"}
        finally:
            if self.process:
                self.process.terminate()

    async def test_list_tools(self):
        """Test the list_tools endpoint."""
        print("\n🔧 Testing list_tools...")
        request = {
            "method": "tools/list",
            "params": {}
        }
        
        response = await self.send_mcp_request(request)
        
        if "error" in response:
            print(f"❌ Error: {response['error']}")
            return False
            
        if "result" in response and "tools" in response["result"]:
            tools = response["result"]["tools"]
            print(f"✅ Found {len(tools)} tool(s):")
            for tool in tools:
                print(f"   • {tool['name']}: {tool['description']}")
            return True
        else:
            print(f"❌ Unexpected response format: {response}")
            return False

    async def test_geocoding_tool(self, location: str):
        """Test the get_coordinates tool."""
        print(f"\n📍 Testing get_coordinates with '{location}'...")
        
        request = {
            "method": "tools/call",
            "params": {
                "name": "get_coordinates",
                "arguments": {
                    "location": location,
                    "limit": 1
                }
            }
        }
        
        response = await self.send_mcp_request(request)
        
        if "error" in response:
            print(f"❌ Error: {response['error']}")
            return False
            
        if "result" in response and "content" in response["result"]:
            content = response["result"]["content"]
            if content and len(content) > 0:
                result_text = content[0].get("text", "")
                try:
                    result_data = json.loads(result_text)
                    if "error" in result_data:
                        print(f"⚠️  Geocoding error: {result_data['error']}")
                    else:
                        print(f"✅ Success! Found {result_data.get('results_count', 0)} result(s)")
                        if "coordinates" in result_data:
                            for coord in result_data["coordinates"][:1]:  # Show first result
                                print(f"   📍 {coord['display_name']}")
                                print(f"   🌍 Lat: {coord['latitude']}, Lng: {coord['longitude']}")
                    return True
                except json.JSONDecodeError:
                    print(f"❌ Invalid JSON in response: {result_text}")
                    return False
            else:
                print(f"❌ No content in response")
                return False
        else:
            print(f"❌ Unexpected response format: {response}")
            return False

async def main():
    """Run all MCP tests."""
    
    print("🧪 MCP Geocoding Server Test Suite")
    print("=" * 50)
    
    # Check if server file exists
    server_path = "geocoding_server.py"
    try:
        with open(server_path, 'r') as f:
            pass
    except FileNotFoundError:
        print(f"❌ Server file '{server_path}' not found!")
        print("   Make sure you're running this in the same directory as geocoding_server.py")
        return
    
    tester = MCPTester(server_path)
    
    # Test 1: List tools
    tools_success = await tester.test_list_tools()
    
    if not tools_success:
        print("\n❌ list_tools test failed - aborting further tests")
        return
    
    # Test 2: Test geocoding with various locations
    test_locations = [
        "New York",
        "London, UK",
        "InvalidLocation12345"
    ]
    
    successful_tests = 0
    total_tests = len(test_locations)
    
    for location in test_locations:
        success = await tester.test_geocoding_tool(location)
        if success:
            successful_tests += 1
    
    # Summary
    print(f"\n{'='*50}")
    print(f"🎯 Test Results: {successful_tests}/{total_tests + 1} tests passed")
    
    if successful_tests == total_tests and tools_success:
        print("🎉 All tests passed! Your MCP server is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the errors above.")

if __name__ == "__main__":
    asyncio.run(main())
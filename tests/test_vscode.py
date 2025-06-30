#!/usr/bin/env python3

"""
VSCode Terminal Test Script for MCP Geocoding Server
Run this in VSCode's integrated terminal to verify everything works
"""

import asyncio
import json
import subprocess
import sys
import os
from pathlib import Path
import time

class VSCodeMCPTester:
    def __init__(self):
        self.project_root = Path.cwd()
        self.server_file = self.project_root / "geocoding_server.py"
        self.vscode_dir = self.project_root / ".vscode"
        self.mcp_config = self.vscode_dir / "mcp.json"

    def print_header(self, title):
        """Print a nice header for test sections."""
        print(f"\n{'='*60}")
        print(f"🧪 {title}")
        print('='*60)

    def print_step(self, step, description):
        """Print a test step."""
        print(f"\n{step}. {description}")
        print("-" * 40)

    def check_prerequisites(self):
        """Check if all required files and dependencies exist."""
        self.print_header("Checking Prerequisites")
        
        checks = [
            ("📁 Project structure", self.project_root.exists()),
            ("🐍 MCP server file", self.server_file.exists()),
            ("📂 .vscode directory", self.vscode_dir.exists()),
            ("⚙️  MCP configuration", self.mcp_config.exists()),
        ]
        
        all_good = True
        for check_name, result in checks:
            status = "✅" if result else "❌"
            print(f"{status} {check_name}")
            if not result:
                all_good = False
        
        # Check Python dependencies
        try:
            import mcp
            print("✅ MCP library installed")
        except ImportError:
            print("❌ MCP library missing - run: pip install mcp")
            all_good = False
            
        try:
            import aiohttp
            print("✅ aiohttp library installed")
        except ImportError:
            print("❌ aiohttp library missing - run: pip install aiohttp")
            all_good = False
        
        return all_good

    def create_vscode_config(self):
        """Create VSCode MCP configuration if it doesn't exist."""
        self.print_step("1", "Creating VSCode MCP Configuration")
        
        # Create .vscode directory
        self.vscode_dir.mkdir(exist_ok=True)
        
        # MCP configuration
        config = {
            "servers": {
                "geocoding": {
                    "command": "python",
                    "args": ["geocoding_server.py"],
                    "cwd": "${workspaceFolder}",
                    "env": {
                        "DEBUG": "1",
                        "PYTHONUNBUFFERED": "1"
                    }
                }
            }
        }
        
        with open(self.mcp_config, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✅ Created {self.mcp_config}")
        print(f"📄 Config contents:")
        print(json.dumps(config, indent=2))

    async def test_server_startup(self):
        """Test if the MCP server starts up correctly."""
        self.print_step("2", "Testing Server Startup")
        
        try:
            # Start the server process
            process = subprocess.Popen(
                [sys.executable, str(self.server_file)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=str(self.project_root)
            )
            
            # Give it a moment to start
            await asyncio.sleep(1)
            
            # Check if it's still running
            if process.poll() is None:
                print("✅ Server started successfully")
                process.terminate()
                await asyncio.sleep(0.5)
                return True
            else:
                stdout, stderr = process.communicate()
                print("❌ Server failed to start")
                if stderr:
                    print(f"Error: {stderr}")
                return False
                
        except Exception as e:
            print(f"❌ Exception starting server: {e}")
            return False

    async def test_mcp_protocol(self):
        """Test basic MCP protocol communication."""
        self.print_step("3", "Testing MCP Protocol Communication")
        
        # Test list_tools request
        list_tools_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list",
            "params": {}
        }
        
        try:
            process = subprocess.Popen(
                [sys.executable, str(self.server_file)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=str(self.project_root)
            )
            
            # Send request
            request_json = json.dumps(list_tools_request) + "\n"
            stdout, stderr = process.communicate(input=request_json, timeout=5)
            
            # Parse response
            if stdout.strip():
                try:
                    response = json.loads(stdout.strip())
                    if "result" in response and "tools" in response["result"]:
                        tools = response["result"]["tools"]
                        print(f"✅ MCP protocol working - found {len(tools)} tool(s)")
                        for tool in tools:
                            print(f"   🔧 {tool['name']}: {tool['description']}")
                        return True
                    else:
                        print(f"❌ Unexpected response format: {response}")
                        return False
                except json.JSONDecodeError as e:
                    print(f"❌ Invalid JSON response: {e}")
                    print(f"Raw output: {stdout}")
                    return False
            else:
                print("❌ No response from server")
                if stderr:
                    print(f"Error output: {stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print("❌ Server request timed out")
            process.kill()
            return False
        except Exception as e:
            print(f"❌ Exception during protocol test: {e}")
            return False

    async def test_geocoding_function(self):
        """Test the actual geocoding functionality."""
        self.print_step("4", "Testing Geocoding Functionality")
        
        # Test get_coordinates request
        geocoding_request = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": "get_coordinates",
                "arguments": {
                    "location": "Paris, France",
                    "limit": 1
                }
            }
        }
        
        try:
            process = subprocess.Popen(
                [sys.executable, str(self.server_file)],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=str(self.project_root)
            )
            
            # Send request
            request_json = json.dumps(geocoding_request) + "\n"
            stdout, stderr = process.communicate(input=request_json, timeout=10)
            
            # Parse response
            if stdout.strip():
                try:
                    response = json.loads(stdout.strip())
                    if "result" in response and "content" in response["result"]:
                        content = response["result"]["content"][0]["text"]
                        result_data = json.loads(content)
                        
                        if "error" in result_data:
                            print(f"⚠️  Geocoding error: {result_data['error']}")
                            return False
                        else:
                            coords = result_data["coordinates"][0]
                            print(f"✅ Geocoding successful!")
                            print(f"   📍 Location: {coords['display_name']}")
                            print(f"   🌍 Coordinates: {coords['latitude']}, {coords['longitude']}")
                            return True
                    else:
                        print(f"❌ Unexpected response: {response}")
                        return False
                except json.JSONDecodeError as e:
                    print(f"❌ Invalid JSON in response: {e}")
                    return False
            else:
                print("❌ No response from geocoding test")
                return False
                
        except subprocess.TimeoutExpired:
            print("❌ Geocoding request timed out")
            process.kill()
            return False
        except Exception as e:
            print(f"❌ Exception during geocoding test: {e}")
            return False

    def print_vscode_instructions(self):
        """Print instructions for using the server in VSCode."""
        self.print_header("VSCode Integration Instructions")
        
        instructions = [
            "1. 🔄 Restart VSCode to pick up the new MCP configuration",
            "2. 🤖 Open Copilot Chat (Ctrl+Alt+I or sidebar icon)",
            "3. 🎯 Switch to 'Agent' mode in the dropdown",
            "4. 🔧 Click the Tools icon to verify geocoding tool appears",
            "5. 💬 Test with prompts like:",
            "   • 'Get coordinates for Tokyo, Japan'",
            "   • 'What's the latitude and longitude of London?'",
            "   • 'Find coordinates for multiple cities'"
        ]
        
        for instruction in instructions:
            print(instruction)
        
        print(f"\n🎉 Your MCP server is ready to use in VSCode!")

async def main():
    """Run all tests."""
    tester = VSCodeMCPTester()
    
    print("🚀 VSCode MCP Geocoding Server Test Suite")
    print("This will verify your MCP server works with VSCode")
    
    # Check prerequisites
    if not tester.check_prerequisites():
        print("\n❌ Prerequisites not met. Please fix the issues above and try again.")
        return
    
    # Create/update VSCode configuration
    tester.create_vscode_config()
    
    # Run tests
    tests = [
        ("Server Startup", tester.test_server_startup()),
        ("MCP Protocol", tester.test_mcp_protocol()),
        ("Geocoding Function", tester.test_geocoding_function())
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_coro in tests:
        try:
            result = await test_coro
            if result:
                passed += 1
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
    
    # Print results
    print(f"\n{'='*60}")
    print(f"🎯 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your MCP server is ready for VSCode.")
        tester.print_vscode_instructions()
    else:
        print("⚠️  Some tests failed. Check the errors above.")
        print("💡 Make sure you have all dependencies installed:")
        print("   pip install mcp aiohttp")

if __name__ == "__main__":
    asyncio.run(main())
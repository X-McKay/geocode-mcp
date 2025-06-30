# Tests

This directory contains all test files for the geocode-mcp project.

## Test Files

### Core Tests
- **`test_geocoding.py`** - Unit tests for the geocoding functionality
- **`test_mcp.py`** - Unit tests for the MCP server functionality
- **`test_mcp_server.py`** - Integration test for the MCP server protocol

### Integration Tests
- **`test_vscode.py`** - VSCode integration tests and setup

## Running Tests

### All Tests
```bash
make test
```

### Specific Test Files
```bash
# Run only geocoding tests
pytest tests/test_geocoding.py -v

# Run only MCP server tests
pytest tests/test_mcp.py -v

# Run VSCode integration tests
python tests/test_vscode.py

# Run MCP server integration test
python tests/test_mcp_server.py
```

### With Coverage
```bash
make test-cov
```

## Test Categories

### Unit Tests
- **`test_geocoding.py`**: Tests the core geocoding functionality using mocked HTTP responses
- **`test_mcp.py`**: Tests the MCP server API and tool handling

### Integration Tests
- **`test_mcp_server.py`**: Tests the full MCP server protocol communication
- **`test_vscode.py`**: Tests VSCode MCP integration and configuration

## Test Dependencies

All tests require the development dependencies:
```bash
make install-dev
```

## Writing New Tests

When adding new tests:
1. Follow the existing naming convention: `test_*.py`
2. Use pytest for unit tests
3. Use async/await for MCP server tests
4. Mock external dependencies (HTTP requests, etc.)
5. Add type annotations for all test functions 
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2025-07-02

### Added
- Configuration examples for Cursor, VS Code, and Claude Desktop
- Comprehensive configuration guide in `config/README.md`
- Updated integration documentation for all supported tools
- PyPI package distribution support with `uvx` installation
- Proper entry point script: `geocode-mcp`

### Changed
- **BREAKING**: Tool name changed from `get_coordinates` to `mcp_geocoding_get_coordinates`
- **BREAKING**: Package structure simplified - removed `/scripts/` directory
- Entry point now uses `geocode-mcp` command for consistency
- Updated all documentation to reflect modern installation via PyPI
- Improved project structure documentation
- Enhanced troubleshooting guides for all integrations
- Updated Makefile to remove obsolete commands and fix package references
- Cleaned up development dependencies and configuration

### Removed
- `/scripts/run_mcp_server.py` - replaced with proper entry point
- Obsolete configuration examples with local file paths
- Outdated documentation references

### Fixed
- Package name consistency across all configuration files
- Entry point configuration in `pyproject.toml`
- Documentation links and file references
- Development setup instructions

## [0.1.0] - 2025-06-29

### Added
- Initial release of MCP Geocoding Server
- Geocoding functionality using OpenStreetMap Nominatim API
- Support for multiple result limits
- Detailed location information including bounding boxes
- Comprehensive error handling with suggestions
- MIT License
- Basic documentation and setup instructions

### Features
- `get_coordinates` tool for location-to-coordinates conversion
- Async HTTP requests with proper error handling
- No API key required
- Support for cities, addresses, and general locations
- Configurable result limits (1-10)
- Detailed response format with metadata

[Unreleased]: https://github.com/X-McKay/geocode-mcp/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/X-McKay/geocode-mcp/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/X-McKay/geocode-mcp/releases/tag/v0.1.0

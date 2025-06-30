# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Comprehensive test suite with mocked API responses
- GitHub Actions CI/CD pipeline
- Pre-commit hooks for code quality
- Development dependencies and configuration
- Security policy documentation
- Contributing guidelines

### Changed
- Updated project configuration to use pyproject.toml exclusively
- Improved README with badges and better documentation
- Enhanced error handling and validation

### Fixed
- Consistent package naming across configuration files

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

[Unreleased]: https://github.com/[username]/geocode-mcp/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/[username]/geocode-mcp/releases/tag/v0.1.0

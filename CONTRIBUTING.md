# Contributing to MCP Geocoding Server

Thank you for your interest in contributing to the MCP Geocoding Server! We welcome contributions from the community.

## Ways to Contribute

- **Bug Reports**: Report bugs by opening an issue
- **Feature Requests**: Suggest new features through issues
- **Code Contributions**: Submit pull requests with improvements
- **Documentation**: Help improve documentation and examples

## Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/X-McKay/geocode-mcp.git
   cd geocode-mcp
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -e .
   pip install pytest  # For running tests
   ```

4. **Run tests**:
   ```bash
   python -m pytest tests/
   ```

## Code Style

- Follow PEP 8 Python style guidelines
- Use type hints where appropriate
- Add docstrings to new functions and classes
- Keep functions focused and well-documented

## Pull Request Process

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** with appropriate tests
4. **Run tests** to ensure everything works
5. **Commit** with clear, descriptive messages
6. **Push** to your fork and submit a pull request

## Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Include tests for new functionality
- Update documentation if needed
- Ensure all tests pass

## Reporting Issues

When reporting bugs, please include:

- **Description**: Clear description of the issue
- **Steps to reproduce**: Detailed steps to recreate the problem
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Environment**: Python version, OS, MCP client being used
- **Error messages**: Full error messages and stack traces

## Code of Conduct

Please be respectful and constructive in all interactions. We want to maintain a welcoming environment for all contributors.

## Questions?

Feel free to open an issue for questions about contributing or using the server.

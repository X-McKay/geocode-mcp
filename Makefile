.PHONY: help install install-dev clean lint format check test test-cov type-check all check-all

# Default target
help:
	@echo "Available commands:"
	@echo "  install      - Install production dependencies"
	@echo "  install-dev  - Install development dependencies"
	@echo "  clean        - Remove Python cache files"
	@echo "  lint         - Run ruff linter"
	@echo "  format       - Format code with ruff"
	@echo "  check        - Run ruff check (lint + format check)"
	@echo "  test         - Run tests"
	@echo "  test-cov     - Run tests with coverage"
	@echo "  type-check   - Run type checking with ty"
	@echo "  all          - Run lint, format, type-check, and test"
	@echo "  check-all    - Run all checks (lint, format, type-check)"

# Install production dependencies
install:
	pip install -e .

# Install development dependencies
install-dev:
	pip install -e ".[dev]"

# Clean Python cache files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +

# Run ruff linter
lint:
	ruff check src/ tests/

# Format code with ruff
format:
	ruff format src/ tests/

# Run ruff check (lint + format check)
check:
	ruff check --fix src/ tests/
	ruff format --check src/ tests/

# Run tests
test:
	pytest tests/ -v

# Run tests with coverage
test-cov:
	pytest tests/ --cov=src/geocode --cov-report=term-missing --cov-report=html -v

# Run type checking with ty
type-check:
	.venv/bin/python -m ty check src/ tests/

# Run all checks (lint, format, type-check, test)
all: lint format type-check test

# Run all checks without tests
check-all: lint format type-check 
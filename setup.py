#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="mcp-geocoding-server",
    version="0.1.0",
    description="MCP server for geocoding cities and locations to latitude/longitude coordinates",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/mcp-geocoding-server",
    packages=find_packages(),
    install_requires=[
        "mcp>=1.0.0",
        "aiohttp>=3.8.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "mcp-geocoding-server=geocoding_server:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="mcp geocoding coordinates latitude longitude openstreetmap",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
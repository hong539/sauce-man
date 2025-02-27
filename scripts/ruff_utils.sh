#!/usr/bin/env bash
set -euxo pipefail

uvx ruff check   # Lint all files in the current directory.
uvx ruff format  # Format all files in the current directory.
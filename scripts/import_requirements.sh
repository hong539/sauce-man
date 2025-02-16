#!/usr/bin/env bash
set -euxo pipefail

uv pip compile pyproject.toml -o requirements.txt
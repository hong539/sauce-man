#!/usr/bin/env bash
set -euxo pipefail

# uv run fastapi dev test/fast-api-example01.py --host 0.0.0.0 --port 12000

# uv run fastapi dev test/fastapi-discord.py --host 0.0.0.0 --port 12000

uv run fastapi dev test/fastapi-discord-02.py --host 0.0.0.0 --port 12000
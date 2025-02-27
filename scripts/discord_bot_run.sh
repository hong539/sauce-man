#!/usr/bin/env bash
set -euxo pipefail

cd "$(dirname "$0")/../backend"
export PYTHONPATH=$(pwd)

# dev with uv
uv run --env-file backend/bot/.env backend/bot/main.py

# deploy with docker/podman container 
# docker run -d --env-file=.env --name sauce_man docker.io/focal1119/sauce_man:test

# podman run -d --env-file=.env --name sauce_man docker.io/focal1119/sauce_man:test
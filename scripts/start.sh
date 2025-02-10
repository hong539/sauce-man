#!/usr/bin/env bash
set -euxo pipefail

# dev with uv
uv run --env-file .env src/main.py

# deploy with docker/podman container 
# docker run -d --env-file=.env --name sauce_man docker.io/focal1119/sauce_man:test

# podman run -d --env-file=.env --name sauce_man docker.io/focal1119/sauce_man:test
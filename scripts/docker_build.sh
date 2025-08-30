#!/usr/bin/env bash
set -euxo pipefail

TAG=$(date +"%Y-%m-%d-%H-%M")

# cd backend/bot
# uv pip compile pyproject.toml > requirements.txt
docker build -f bot/Dockerfile.bot -t docker.io/focal1119/sauce-man-bot:$TAG .
#!/usr/bin/env bash
set -euxo pipefail

TAG=$(date +"%Y-%m-%d-%H-%M")

docker build -f Dockerfile.bot -t docker.io/focal1119/sauce-man-bot:$TAG .
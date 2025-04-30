#!/usr/bin/env bash
set -euxo pipefail

podman build . -t docker.io/focal1119/sauce-man:test
podman build . --no-cache -t docker.io/focal1119/sauce-man:test
podman run -d --env-file=.env --name sauce-man docker.io/focal1119/sauce-man:test
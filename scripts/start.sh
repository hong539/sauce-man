#!/usr/bin/env bash
set -euxo pipefail

podman run -d --env-file=.env --name sauce_man docker.io/focal1119/sauce_man:test
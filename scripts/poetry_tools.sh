#!/usr/bin/env bash
set -euxo pipefail

#poetry self add poetry-plugin-export
# poetry self add poetry-plugin-shell

# poetry env use 3.10.14

cat requirements.txt | xargs poetry add
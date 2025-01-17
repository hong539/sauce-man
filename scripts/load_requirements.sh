#!/usr/bin/env bash
set -euxo pipefail

cat requirements.txt | xargs poetry add
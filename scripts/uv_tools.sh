#!/usr/bin/env bash
set -euxo pipefail

#install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version

#generate-shell-completion
echo -e 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
source ~/.bashrc

#init
uv init

#dependencies check
uv pip check

#sync
uv sync

#Use a specific Python version in the current directory:
uv python pin 3.10

#Viewing Python installations
uv python list

#Importing dependencies
#docs: https://docs.astral.sh/uv/concepts/projects/dependencies/#importing-dependencies
uv add -r requirements.txt
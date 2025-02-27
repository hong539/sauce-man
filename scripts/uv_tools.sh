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

uv python uninstall 3.11

#cache
uv cache dir
uv cache clean

#Exporting dependencies
# uv pip freeze > requirements.txt
# uv pip freeze --project pyproject.toml
uv pip compile pyproject.toml > requirements.txt

#Importing dependencies
#docs: https://docs.astral.sh/uv/concepts/projects/dependencies/#importing-dependencies
uv add -r requirements.txt

# sauce-man root
uv add backend/api backend/core backend/bot

# core
uv add pydantic
uv add pydantic-settings
uv add sqlalchemy

# bot
uv add discord-py
uv add pydantic
uv add pydantic-settings

# backend/api
uv add fastapi --extra standard
uv add pydantic
uv add pydantic-settings
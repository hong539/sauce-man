import toml

# Load pyproject.toml
with open("pyproject.toml", "r") as f:
    data = toml.load(f)

# Migrate tool.poetry to project
tool_poetry = data.pop("tool", {}).get("poetry", {})
data["project"] = {
    "name": tool_poetry.get("name"),
    "version": tool_poetry.get("version"),
    "description": tool_poetry.get("description"),
    "readme": tool_poetry.get("readme"),
    "license": {"text": tool_poetry.get("license")},
    "authors": tool_poetry.get("authors"),
    "scripts": {k: {"callable": v} for k, v in tool_poetry.get("scripts", {}).items()},
}

# Save the updated pyproject.toml
with open("pyproject.toml", "w") as f:
    toml.dump(data, f)

print("Updated pyproject.toml for Poetry 2.0+!")

import os
import json

# 設定 .vscode 目錄和設定檔路徑
vscode_dir = ".vscode"
settings_path = os.path.join(vscode_dir, "settings.json")

# 設定內容
settings_content = {
    "python.pythonPath": ".venv/bin/python",  # 對應 Poetry 的虛擬環境
    "python.formatting.provider": "black",
    "python.linting.enabled": True,
    "python.linting.pylintEnabled": True,
    "python.testing.unittestEnabled": False,
    "python.testing.pytestEnabled": True,
    "python.testing.pytestArgs": ["tests"],
}

# 確保 .vscode 目錄存在
os.makedirs(vscode_dir, exist_ok=True)

# 寫入設定檔
with open(settings_path, "w") as f:
    json.dump(settings_content, f, indent=4)

print(f"Generated VS Code settings at {settings_path}")

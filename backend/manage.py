#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess

# 設定 BASE_DIR 為 backend/
# 確保 backend 是 PYTHONPATH 的第一個目錄
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

# 設定環境變數
CORE_ENV_FILE = os.path.join(BASE_DIR, "core", ".env")
BACKEND_ENV_FILE = os.path.join(BASE_DIR, ".env")

if os.path.exists(CORE_ENV_FILE):
    ENV_FILE = CORE_ENV_FILE
elif os.path.exists(BACKEND_ENV_FILE):
    ENV_FILE = BACKEND_ENV_FILE
else:
    ENV_FILE = None
    print("[警告] 找不到 `.env` 檔案，將使用系統環境變數。")

def run_api(host: str, port: int, use_uv: bool):
    """運行 FastAPI 應用"""
    if use_uv:
        # 使用 uv 執行 FastAPI，並確保 cwd 在 backend
        cmd = ["uv", "run", "--python=python3.11"]
        if ENV_FILE:
            cmd += ["--env-file", ENV_FILE]
        cmd += ["main.py", host, str(port)]
    else:
        # 部署環境使用 fastapi run
        cmd = ["fastapi", "run", "--host", host, "--port", str(port)]

    subprocess.run(cmd, cwd=os.path.join(BASE_DIR, "api"))  # 強制工作目錄為 backend/api/

def run_bot(use_uv: bool):
    """運行 Discord Bot"""
    if use_uv:
        # 使用 uv 執行 Discord Bot
        cmd = ["uv", "run", "--python=python3.11"]
        if ENV_FILE:
            cmd += ["--env-file", ENV_FILE]
        cmd += ["main.py"]
    else:
        # 部署環境使用 discord-bot run
        cmd = ["discord-bot", "run"]

    subprocess.run(cmd, cwd=os.path.join(BASE_DIR, "bot"))  # 強制工作目錄為 backend/bot/

def main():
    parser = argparse.ArgumentParser(description="Manage the application")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 運行 FastAPI
    api_parser = subparsers.add_parser("runapi", help="Run FastAPI server")
    api_parser.add_argument("host", type=str, help="Host address (e.g., 0.0.0.0)")
    api_parser.add_argument("port", type=int, help="Port number (e.g., 8000)")
    api_parser.add_argument("--uv", action="store_true", help="Use uv for development")

    # 運行 Discord Bot
    bot_parser = subparsers.add_parser("runbot", help="Run Discord bot")
    bot_parser.add_argument("--uv", action="store_true", help="Use uv for development")

    args = parser.parse_args()

    if args.command == "runapi":
        run_api(args.host, args.port, args.uv)
    elif args.command == "runbot":
        run_bot(args.uv)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import os
import sys
import argparse
import subprocess

# 設定 backend 為 PYTHONPATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "core"))

def run_api(host: str, port: int, use_uv: bool):
    """運行 FastAPI 應用"""
    if use_uv:
        cmd = ["uv", "run", "-m", "api.main"]
    else:
        cmd = ["uvicorn", "api.main:app", "--host", host, "--port", str(port), "--reload"]
    
    subprocess.run(cmd, cwd=BASE_DIR)

def run_bot(use_uv: bool):
    """運行 Discord Bot"""
    if use_uv:
        cmd = ["uv", "run", "-m", "bot.main"]
    else:
        cmd = ["python3", "-m", "bot.main"]
    
    subprocess.run(cmd, cwd=BASE_DIR)

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
import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# need to right path for .env file
# 確保 `.env` 使用絕對路徑，避免找不到
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# ENV_PATH = os.path.join(BASE_DIR, ".env")

# 專案根：.../bot
ROOT_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT_DIR / ".env"

class Settings(BaseSettings):
    """管理環境變數的設定類"""

    # Discord Bot 設定
    token: str
    guild_id: int

    # FastAPI 設定
    api_host: str
    api_port: int
    api_url: str

    # 資料庫設定
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    # 指定 `.env` 檔案（完整路徑，避免找不到）
    model_config = SettingsConfigDict(env_file=ENV_PATH, env_file_encoding="utf-8")

# 初始化設定
settings = Settings()

TOKEN = settings.token
GUILD_ID = settings.guild_id

DB_USER = settings.db_user
DB_PASSWORD = settings.db_password
DB_HOST = settings.db_host
DB_PORT = settings.db_port
DB_NAME = settings.db_name

# 可以動態選擇要啟用哪些指令
ENABLED_COMMANDS = ["hello", "add", "send"]  # 只載入這三個指令

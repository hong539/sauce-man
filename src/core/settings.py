from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """管理環境變數的設定類"""
    
    # Discord Bot 設定
    token: str
    guild_id: int

    # FastAPI 設定
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # 資料庫設定
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    # 指定 `.env` 檔案（與 dotenv 不同，這是 Pydantic 內建支持）
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# 初始化設定
settings = Settings()

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DB_USER: str = "your_user"
    DB_HOST: str = "your_host"
    DB_PASSWORD: str = "your_password"
    DB_PORT: str = "your_port"
    DB_NAME: str = "your_db"

    class Config:
        env_file = ".env"


settings = Settings()

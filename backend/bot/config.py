from core.settings import settings

TOKEN = settings.token
GUILD_ID = settings.guild_id

DB_USER = settings.db_user
DB_PASSWORD = settings.db_password
DB_HOST = settings.db_host
DB_PORT = settings.db_port
DB_NAME = settings.db_name

# 可以動態選擇要啟用哪些指令
ENABLED_COMMANDS = ["hello", "add", "send"]  # 只載入這三個指令

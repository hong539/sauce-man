import os
import datetime
import asyncio
import discord
from discord import app_commands
import pandas as pd
from sqlalchemy import create_engine
from fastapi import FastAPI
import uvicorn

TOKEN = os.environ['TOKEN']
GUILD_ID = os.environ['GUILD_ID']

# ✅ 創建 FastAPI 應用
app = FastAPI()

class MyClient(discord.Client):
    
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)        
        self.token = TOKEN
        self.guild_id = GUILD_ID        
        self.tree = app_commands.CommandTree(self)
        self.guild = discord.Object(id=int(self.guild_id))  

    async def setup_hook(self):
        self.tree.copy_global_to(guild=self.guild)
        await self.tree.sync(guild=self.guild)
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        print(f'Message from {message.channel}:{message.author}: {message.content}')


# ✅ 創建 Discord Bot
client = MyClient()

# ✅ 創建 Web API
@app.get("/")
def home():
    return {"message": "Hello from FastAPI & Discord Bot"}

@app.get("/bot/status")
def bot_status():
    """查詢 Discord Bot 狀態"""
    return {
        "bot_name": client.user.name if client.user else "Not logged in",
        "bot_id": client.user.id if client.user else "N/A",
        "guild_id": client.guild_id
    }

@app.post("/send-message/{channel_id}")
async def send_message(channel_id: int, message: str):
    """透過 API 指定 Bot 發送訊息到某個頻道"""
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send(message)
        return {"status": "success", "message": f"Sent to channel {channel_id}"}
    return {"status": "error", "message": "Invalid channel ID"}

# ✅ 讓 Discord Bot 和 FastAPI 共同運行
async def run_discord_bot():
    """運行 Discord Bot"""
    await client.start(TOKEN)

def main():
    """同時運行 FastAPI & Discord Bot"""
    loop = asyncio.get_event_loop()
    loop.create_task(run_discord_bot())  # 讓 Discord Bot 運行
    uvicorn.run(app, host="0.0.0.0", port=8000)  # 讓 FastAPI 運行

if __name__ == "__main__":
    main()
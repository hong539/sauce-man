from .client import client


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")


@client.event
async def on_message(message):
    print(f"Message from {message.channel}: {message.author}")  # **避免洩漏訊息內容**

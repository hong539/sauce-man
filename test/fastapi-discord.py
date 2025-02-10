import asyncio
import discord
from fastapi import FastAPI

app = FastAPI()
client = discord.Client()


# where the magic happens
# register an asyncio.create_task(client.start()) on app's startup event
#                                        ^ note not client.run()
@app.on_event("startup")
async def startup_event():
  asyncio.create_task(client.start('token'))


@app.get("/")
async def read_root():
  return {"Hello": str(client.user)}
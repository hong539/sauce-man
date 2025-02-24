from .client import client
from discord import app_commands
from typing import Optional
import discord
import datetime
import pandas as pd
from sqlalchemy import create_engine
from .config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

@client.tree.command()
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@client.tree.command()
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')

@client.tree.command()
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    """Says when a member joined."""
    member = member or interaction.user
    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

@client.tree.command()
async def dump_oldest_message(interaction: discord.Interaction, member: Optional[discord.Member] = None, channel: Optional[discord.TextChannel] = None, before_date: Optional[str] = None, after_date: Optional[str] = None):
    """Dump messages from a channel with a member from oldest to current."""
    db_connect_info = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(db_connect_info)
    df = pd.DataFrame(columns=['message'])
    before_date = datetime.datetime.fromisoformat(before_date) if before_date else None
    after_date = datetime.datetime.fromisoformat(after_date) if after_date else None
    member = member or interaction.user
    counter = 0
    contents = []
    async for message in channel.history(limit=None, before=before_date, after=after_date, oldest_first=True):
        counter += 1
        contents.append(message.content)

    df['message'] = contents
    df.to_sql(name=channel.name, con=engine, if_exists='append', index=False)
    await interaction.response.send_message(f'Dumped {counter} messages from {member} in {channel.name}')
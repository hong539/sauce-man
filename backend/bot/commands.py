from discord import app_commands
from typing import Optional
import discord
import datetime
import pandas as pd
# from sqlalchemy import create_engine
# from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

client: Optional[discord.Client] = None

def set_client(c):
    """這個函式讓 main.py 設定 client 物件"""
    global client
    client = c

def register_commands():
    """註冊 Slash 指令"""
    if client is None or not hasattr(client, "tree"):
        raise ValueError("client 尚未設定或 `client.tree` 尚未初始化！")

    command_registry = {
        "hello": hello,
        "add": add,
        "send": send,
        "joined": joined,
        "search_oldest_message": search_oldest_message,
        # "dump_oldest_message": dump_oldest_message,
    }

    for cmd_name in command_registry:
        client.tree.add_command(command_registry[cmd_name])

    print("Slash 指令已成功註冊！")

def register_context_menus():
    """註冊 Context Menu 指令"""
    if client is None or not hasattr(client, "tree"):
        raise ValueError("client 尚未設定或 `client.tree` 尚未初始化！")

    # client.tree.add_command(app_commands.ContextMenu(name="Show Join Date", callback=show_join_date))
    # client.tree.add_command(app_commands.ContextMenu(name="Report to Moderators", callback=report_message))

    print("Context Menu 指令已成功註冊！")

async def sync_commands():
    """同步所有應用指令到 Discord"""
    if client is None or not hasattr(client, "tree"):
        raise ValueError("client 尚未設定或 `client.tree` 尚未初始化！")

    await client.tree.sync()
    print("所有應用指令已同步至 Discord！")

# ========== 指令定義 ========== #
@app_commands.command(name="hello")
async def hello(interaction: discord.Interaction):
    """Says hello!"""
    await interaction.response.send_message(f'Hi, {interaction.user.mention}')

@app_commands.command(name="add")
@app_commands.describe(
    first_value='The first value you want to add something to',
    second_value='The value you want to add to the first value',
)
async def add(interaction: discord.Interaction, first_value: int, second_value: int):
    """Adds two numbers together."""
    await interaction.response.send_message(f'{first_value} + {second_value} = {first_value + second_value}')


# The rename decorator allows us to change the display of the parameter on Discord.
# In this example, even though we use `text_to_send` in the code, the client will use `text` instead.
# Note that other decorators will still refer to it as `text_to_send` in the code.
@app_commands.command(name="send")
@app_commands.rename(text_to_send='text')
@app_commands.describe(text_to_send='Text to send in the current channel')
async def send(interaction: discord.Interaction, text_to_send: str):
    """Sends the text into the current channel."""
    await interaction.response.send_message(text_to_send)


# To make an argument optional, you can either give it a supported default argument
# or you can mark it as Optional from the typing standard library. This example does both.
@app_commands.command(name="joined")
@app_commands.describe(member='The member you want to get the joined date from; defaults to the user who uses the command')
async def joined(interaction: discord.Interaction, member: Optional[discord.Member] = None):
    """Says when a member joined."""
    # If no member is explicitly provided then we use the command user here
    member = member or interaction.user

    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} joined {discord.utils.format_dt(member.joined_at)}')


# A Context Menu command is an app command that can be run on a member or on a message by
# accessing a menu within the client, usually via right clicking.
# It always takes an interaction as its first parameter and a Member or Message as its second parameter.

# This context menu command only works on members
@app_commands.command(name="show_join_date")
async def show_join_date(interaction: discord.Interaction, member: discord.Member):
    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')


# # This context menu command only works on messages
# @app_commands.command(name="report_message")
# async def report_message(interaction: discord.Interaction, message: discord.Message):
#     # We're sending this response message with ephemeral=True, so only the command executor can see it
#     await interaction.response.send_message(
#         f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
#     )

#     # Handle report by sending it into a log channel
#     log_channel = interaction.guild.get_channel(0)  # replace with your channel id

#     embed = discord.Embed(title='Reported Message')
#     if message.content:
#         embed.description = message.content

#     embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
#     embed.timestamp = message.created_at

#     url_view = discord.ui.View()
#     url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

#     await log_channel.send(embed=embed, view=url_view)

@app_commands.command(name="search_oldest_message")
@app_commands.describe(member='The member you want to search',
                        channel='The channel you want to search'
                        )
async def search_oldest_message(interaction: discord.Interaction, member: Optional[discord.Member] = None, channel: Optional[discord.TextChannel] = None):
    """Search an oldest message from a channel with a member."""
    member = member or interaction.user
    async for messages in channel.history(limit=1, oldest_first=True):
        content = messages.content
        jump_url = messages.jump_url
    await interaction.response.send_message(f'member: {member} in channel: {channel}: send an oldest message: {content} at jump_url: {jump_url}')
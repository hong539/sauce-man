import os
import datetime
from pathlib import Path
from typing import Optional
import discord
from discord import app_commands
import yaml
import pandas as pd
from sqlalchemy import create_engine

def load_config(path: str) -> dict:
    """Load configuration data from a YAML file.

    Args:
        path (str): The path to the YAML configuration file.
    """
    with open(path, "r") as config:
        config_data = yaml.safe_load(config)
        print("config_data loading OK!")
        # print("config_data type is:", type(config_data))
        # print("bot token is:\n", config_data["bot"]["token"])
        # print("discord guild ID is:\n", config_data["bot"]["guild_id"])
    return config_data


class MyClient(discord.Client):
    
    def __init__(self, path: str) -> None:
        # Just default intents and a `discord.Client` instance
        # We don't need a `commands.Bot` instance because we are not
        # creating text-based commands.
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.config_data = load_config(path)
        self.token = self.config_data["bot"]["token"]
        # We need an `discord.app_commands.CommandTree` instance
        # to register application commands (slash commands in this case)
        self.tree = app_commands.CommandTree(self)
        self.guild = discord.Object(id=int(self.config_data["bot"]["guild_id"]))  # replace with your guild id

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=self.guild)
        await self.tree.sync(guild=self.guild)
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        print(f'Message from {message.channel}:{message.author}: {message.content}')

def main():
    
    BASE_DIR = Path(__file__).resolve().parent
    config_path = os.path.join(BASE_DIR, 'my_self.yaml')    
    client = MyClient(config_path)
    
    @client.tree.command()
    async def hello(interaction: discord.Interaction):
        """Says hello!"""
        await interaction.response.send_message(f'Hi, {interaction.user.mention}')

    @client.tree.command()
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
    @client.tree.command()
    @app_commands.rename(text_to_send='text')
    @app_commands.describe(text_to_send='Text to send in the current channel')
    async def send(interaction: discord.Interaction, text_to_send: str):
        """Sends the text into the current channel."""
        await interaction.response.send_message(text_to_send)


    # To make an argument optional, you can either give it a supported default argument
    # or you can mark it as Optional from the typing standard library. This example does both.
    @client.tree.command()
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
    @client.tree.context_menu(name='Show Join Date')
    async def show_join_date(interaction: discord.Interaction, member: discord.Member):
        # The format_dt function formats the date time into a human readable representation in the official client
        await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')


    # This context menu command only works on messages
    @client.tree.context_menu(name='Report to Moderators')
    async def report_message(interaction: discord.Interaction, message: discord.Message):
        # We're sending this response message with ephemeral=True, so only the command executor can see it
        await interaction.response.send_message(
            f'Thanks for reporting this message by {message.author.mention} to our moderators.', ephemeral=True
        )

        # Handle report by sending it into a log channel
        log_channel = interaction.guild.get_channel(0)  # replace with your channel id

        embed = discord.Embed(title='Reported Message')
        if message.content:
            embed.description = message.content

        embed.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
        embed.timestamp = message.created_at

        url_view = discord.ui.View()
        url_view.add_item(discord.ui.Button(label='Go to Message', style=discord.ButtonStyle.url, url=message.jump_url))

        await log_channel.send(embed=embed, view=url_view)

    @client.tree.command()
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

    @client.tree.command()
    @app_commands.describe(member='The member you want to dump',
                           channel='The channel you want to dump',
                           before_date='The date: YYYY-MM-DD you want to dump before',
                           after_date='The date: YYYY-MM-DD you want to dump after'
                          )
    async def dump_oldest_message(interaction: discord.Interaction, member: Optional[discord.Member] = None, channel: Optional[discord.TextChannel] = None, before_date: Optional[str] = None, after_date: Optional[str] = None):
        """Dump messages from a channel with a member from oldest to current."""
        config_data = load_config(config_path)
        engine = create_engine(config_data["database_info"]["connect_str"])
        df = pd.DataFrame(columns=['message'])
        # before_date = datetime.datetime(2021, 7, 31, tzinfo=datetime.timezone.utc)
        # after_date = datetime.datetime(2021, 6, 25, tzinfo=datetime.timezone.utc)
        before_date = datetime.datetime.fromisoformat(before_date) if before_date else None
        after_date = datetime.datetime.fromisoformat(after_date) if after_date else None        
        member = member or interaction.user
        counter = 0
        contents = []
        async for message in channel.history(limit=None, before=before_date, after=after_date, oldest_first=True):
            counter += 1
            contents.append(message.content)

        # print(contents)
        df['message'] = contents
        print("-----------working---------------------------------")
        # print(df)
        df.to_sql(name=channel.name, con=engine, if_exists='append', index=False)
        await interaction.response.send_message(f'Dump messages from {member.nick} in {channel.name}: \n From {after_date} to {before_date} and total message counter: {counter}')
    
    client.run(token= client.token)

if __name__ == "__main__":
    main()
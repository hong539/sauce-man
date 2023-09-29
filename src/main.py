import os
from pathlib import Path
import discord
from discord import app_commands
import yaml

def load_config(path: str) -> dict:
    """Load configuration data from a YAML file.

    Args:
        path (str): The path to the YAML configuration file.
    """
    with open(path, "r") as config:
        config_data = yaml.safe_load(config)
        print("config_data type is:", type(config_data))
        print("bot token is:\n", config_data["bot"]["token"])
        print("discord guild ID is:\n", config_data["bot"]["guild_id"])
    return config_data


class MyClient(discord.Client):
    def __init__(self) -> None:
        # Just default intents and a `discord.Client` instance
        # We don't need a `commands.Bot` instance because we are not
        # creating text-based commands.
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        # We need an `discord.app_commands.CommandTree` instance
        # to register application commands (slash commands in this case)
        self.tree = app_commands.CommandTree(self)
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        print(f'Message from {message.channel}:{message.author}: {message.content}')

def main():
    BASE_DIR = Path(__file__).resolve().parent
    config_path = os.path.join(BASE_DIR, 'my_self.yaml')
    temp = load_config(config_path)
    client = MyClient()
    client.run(token= temp["bot"]["token"])    

if __name__ == "__main__":
    main()
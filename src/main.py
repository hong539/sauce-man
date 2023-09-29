import discord
from discord import app_commands
import yaml

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

    def load_config(self, path):
        """Load configuration data from a YAML file.

        Args:
            path (str): The path to the YAML configuration file.
        """
        with open(path, "r") as config:
            self.config_data = yaml.safe_load(config)
            print("config_data type is:", type(self.config_data))
            print("bot token is:\n", self.config_data["bot"]["token"])
            print("discord guild ID is:\n", self.config_data["bot"]["guild_id"])
        return self.config_data

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        print(f'Message from {message.channel}:{message.author}: {message.content}')
        
        if message.author == client.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

if __name__ == "__main__":
    client = MyClient()
    client.run(token= client.load_config("./my_self.yaml")["bot"]["token"])
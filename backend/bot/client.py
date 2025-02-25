import discord
from discord import app_commands
from config import TOKEN, GUILD_ID

class MyClient(discord.Client):
    
    def __init__(self) -> None:
        # Just default intents and a `discord.Client` instance
        # We don't need a `commands.Bot` instance because we are not
        # creating text-based commands.
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)        
        self.token = TOKEN
        self.guild_id = GUILD_ID        
        # We need an `discord.app_commands.CommandTree` instance
        # to register application commands (slash commands in this case)
        self.tree = app_commands.CommandTree(self)
        self.guild = discord.Object(id=int(self.guild_id))  # replace with your guild id

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
                
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=self.guild)
        await self.tree.sync(guild=self.guild)
        print("Slash 指令已同步！")
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        print(f'Message from {message.channel}:{message.author}: {message.content}')

client = MyClient()
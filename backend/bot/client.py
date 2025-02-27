import discord
from discord import app_commands
from config import TOKEN, GUILD_ID
import commands


class MyClient(discord.Client):
    def __init__(self, load_commands: bool = True) -> None:
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

        self.load_commands = load_commands

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        if self.load_commands:
            commands.set_client(self)  # 設定 client
            commands.register_commands()  # 註冊 Slash 指令
            commands.register_context_menus()  # 註冊 Context Menu 指令
            await commands.sync_commands()  # 同步指令到 Discord
            print("所有 Slash 指令和 Context Menu 指令已載入！")

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    async def on_message(self, message):
        print(f"Message from {message.channel}:{message.author}: {message.content}")


client = MyClient()

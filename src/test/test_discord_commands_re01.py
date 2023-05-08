# src: https://discord.com/developers/docs/getting-started#adding-credentials
# src: https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-structure
# src: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html?highlight=slash#hybrid-commands
# Application Commands
# CHAT_INPUT
# regex
# ^[-_\p{L}\p{N}\p{sc=Deva}\p{sc=Thai}]{1,32}$

from discord.ext import commands

# 建立Discord BOT客戶端
bot = commands.Bot(command_prefix='!')

@bot.hybrid_command()
async def test(ctx):
    await ctx.send("This is a hybrid command!")
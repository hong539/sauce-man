import discord
import requests
from bs4 import BeautifulSoup

# Replace 'your_bot_token' with your actual bot token
TOKEN = 'your_bot_token'

# PTT URL pattern
PTT_URL_PATTERN = r'https://www\.ptt\.cc/bbs/[^/]+/M\.\d+\.A\.\w+\.html'

# Function to fetch and parse PTT content
def fetch_ptt_preview(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Assuming the title is in a specific HTML element, adjust as needed
            title = soup.find('title').text
            return title
        else:
            return "Failed to fetch PTT content."
    except Exception as e:
        return f"Error: {e}"

# Discord bot client
client = discord.Client()

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message contains a PTT URL
    if re.search(PTT_URL_PATTERN, message.content):
        # Extract the first PTT URL from the message
        ptt_url = re.search(PTT_URL_PATTERN, message.content).group(0)
        preview = fetch_ptt_preview(ptt_url)
        await message.channel.send(preview)

# Run the bot
client.run(TOKEN)
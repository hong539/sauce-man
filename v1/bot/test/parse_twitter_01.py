import discord
import aiohttp
import re
import asyncio

TOKEN = "你的Discord Bot Token"

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

TWITTER_ICON_URL = "https://ermiana.canaria.cc/pic/twitter.png"
TWITTER_REGEX = re.compile(r"https?://(?:www\.)?twitter\.com/\w+/status/(\d+)")


async def fetch_twitter_data(api_url):
    """請求 fxtwitter 或 vxtwitter API 獲取推文資訊"""
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url, timeout=2.5) as response:
                if response.status == 200:
                    return await response.json()
        except Exception as e:
            print(f"API 請求錯誤: {e}")
    return None


def create_twitter_embed(
    author_id,
    author_icon,
    author_name,
    tweet_url,
    tweet_text,
    tweet_image,
    tweet_timestamp,
):
    """建立 Discord 內嵌 Embed 訊息"""
    embed = discord.Embed(
        color=0x1DA1F2,
        description=tweet_text,
        timestamp=discord.utils.snowflake_time(tweet_timestamp),
    )
    embed.set_author(name=f"@{author_id}", icon_url=author_icon or "")
    embed.set_title(author_name or "Twitter.com")
    embed.set_url(tweet_url or f"https://twitter.com/i/status/{tweet_timestamp}")
    if tweet_image:
        embed.set_image(url=tweet_image)
    return embed


@client.event
async def on_message(message):
    """監聽 Discord 訊息並處理 Twitter 連結"""
    if message.author.bot:
        return

    match = TWITTER_REGEX.search(message.content)
    if not match:
        return

    tweet_id = match.group(1)
    typing_task = asyncio.create_task(message.channel.typing())

    # 嘗試 fxtwitter API
    fx_url = f"https://api.fxtwitter.com/i/status/{tweet_id}"
    tweet_data = await fetch_twitter_data(fx_url)

    if not tweet_data:
        # 如果 fxtwitter 失敗，改用 vxtwitter API
        vx_url = f"https://api.vxtwitter.com/i/status/{tweet_id}"
        tweet_data = await fetch_twitter_data(vx_url)

    if tweet_data:
        # 解析推文資訊
        author_id = (
            tweet_data.get("user_screen_name")
            or tweet_data["tweet"]["author"]["screen_name"]
        )
        author_icon = (
            tweet_data["tweet"]["author"].get("avatar_url")
            if "tweet" in tweet_data
            else ""
        )
        author_name = (
            tweet_data.get("user_name") or tweet_data["tweet"]["author"]["name"]
        )
        tweet_url = tweet_data.get("tweetURL") or tweet_data["tweet"].get(
            "url", f"https://twitter.com/i/status/{tweet_id}"
        )
        tweet_text = tweet_data.get("text") or tweet_data["tweet"].get("text", "")
        tweet_timestamp = (
            tweet_data.get("date_epoch")
            or tweet_data["tweet"].get("created_timestamp", 0) * 1000
        )

        # 處理圖片 & 影片
        images = []
        videos = []
        if "media_extended" in tweet_data:
            for media in tweet_data["media_extended"]:
                if media["type"] == "image":
                    images.append(media["url"])
                else:
                    videos.append(media["url"])
        elif "tweet" in tweet_data and "media" in tweet_data["tweet"]:
            for media in tweet_data["tweet"]["media"]["all"]:
                if media["type"] == "photo":
                    images.append(media["url"])
                else:
                    videos.append(media["url"])

        # 發送推文 Embed
        embed = create_twitter_embed(
            author_id,
            author_icon,
            author_name,
            tweet_url,
            tweet_text,
            images[0] if images else "",
            tweet_timestamp,
        )
        await message.channel.send(embed=embed)

        # 發送影片連結（如果有的話）
        for video in videos:
            await message.channel.send(f"🎥 影片連結: {video}")

    else:
        # 如果 API 都失敗，發送備用 Twitter 連結
        backup_url = f"https://fxtwitter.com/i/status/{tweet_id}"
        await message.channel.send(f"🔗 推文連結: {backup_url}")

    typing_task.cancel()  # 停止「輸入中」動畫


client.run(TOKEN)

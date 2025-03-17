import aiohttp
import discord

async def handle_twitter_regex(match, message):
    tweet_id = match.group(1)
    api_url = f"https://api.fxtwitter.com/i/status/{tweet_id}"

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url, timeout=2.5) as resp:
                data = await resp.json()

            if "tweet" or "x" not in data:
                await message.channel.send("Twitter 貼文解析失敗！")
                return

            tweet_data = data["tweet"]
            author_name = tweet_data.get("author", {}).get("name", "未知作者")
            author_screen_name = tweet_data.get("author", {}).get("screen_name", "")
            tweet_text = tweet_data.get("text", "無內文")
            tweet_url = tweet_data.get("url", f"https://twitter.com/i/status/{tweet_id}")

            # 解析圖片
            image_url = None
            if "media" in tweet_data:
                if "mosaic" in tweet_data["media"] and tweet_data["media"]["mosaic"]["type"] == "mosaic_photo":
                    image_url = tweet_data["media"]["mosaic"]["formats"]["jpeg"]
                elif "photos" in tweet_data["media"]:
                    image_url = tweet_data["media"]["photos"][0]["url"] + "?name=large"

            # 建立 Embed 訊息
            embed = discord.Embed(title=author_name, url=tweet_url, description=tweet_text, color=0x1DA1F2)
            embed.set_author(name=f"@{author_screen_name}", url=tweet_url)
            if image_url:
                embed.set_image(url=image_url)

            # 發送訊息
            await message.channel.send(embed=embed)

        except Exception as e:
            print(f"Twitter 解析錯誤: {e}")
            await message.channel.send(f"無法獲取 Twitter 貼文: {tweet_id}")
import aiohttp
import discord

async def handle_pixiv_regex(match, message):
    pixiv_id = match.group(1)
    api_url = f"https://www.pixiv.net/ajax/illust/{pixiv_id}"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url, timeout=2.5) as resp:
                data = await resp.json()

            # print(f"Debug pixiv:{data}")
            if 'body' not in data:
                await message.channel.send("Pixiv 圖片解析失敗！")
                return

            pixiv_data = data["body"]
            # print(f"pixiv_data type:{type(pixiv_data)}")
            
            title = pixiv_data.get("title", "無標題")
            user_name = pixiv_data.get("userName", "未知作者")
            user_id = pixiv_data.get("userId", "未知 ID")
            bookmark_count = pixiv_data.get("bookmarkCount", 0)
            tags = [tag["tag"] for tag in pixiv_data.get("tags", {}).get("tags", [])]

            # 解析圖片 URL
            # 修正取得 URL 的方式
            image_url = None

            if "userIllusts" in pixiv_data and pixiv_id in pixiv_data["userIllusts"]:
                image_url = pixiv_data["userIllusts"][pixiv_id].get("url")

            # 替換 Pixiv 網域，避免 CORS 限制
            if image_url:
                image_url = image_url.replace("i.pximg.net", "pixiv.canaria.cc")

            # 建立 Embed 訊息
            embed = discord.Embed(title=title, url=f"https://www.pixiv.net/artworks/{pixiv_id}", color=0x0096fa)
            embed.add_field(name="作者", value=f"[{user_name}](https://www.pixiv.net/users/{user_id})", inline=True)
            embed.add_field(name="收藏", value=str(bookmark_count), inline=True)
            if tags:
                embed.add_field(name="標籤", value=", ".join(tags), inline=False)
            if image_url:
                embed.set_image(url=image_url)

            # 發送訊息
            await message.channel.send(embed=embed)
        except Exception as e:
            print(f"Pixiv 解析錯誤: {e}")
            await message.channel.send(f"無法獲取 Pixiv 圖片: {pixiv_id}")
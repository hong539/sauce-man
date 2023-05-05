import yaml
import discord
from discord.ext import commands
from PIL import Image

def load_config(path):
    with open(path, "r") as config:
        data = yaml.safe_load(config)
        print(type(data))
        print(data["bot"]["token"])
    
    return data

# 建立Discord BOT客戶端
bot = commands.Bot(command_prefix='!')

# 監聽訊息事件
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if len(message.attachments) > 0:
        for attachment in message.attachments:
            # 下載圖片
            await attachment.save(attachment.filename)

            # 圖片旋轉處理
            rotated_image = rotate_image(attachment.filename)

            # 送出旋轉後的圖片
            await message.channel.send(file=discord.File(rotated_image, filename='rotated_image.png'))

            # 圖片辨識
            recognition_result = image_recognition(attachment.filename)

            # 送出圖片辨識結果
            await message.channel.send(f'圖片辨識結果：{recognition_result}')

# 圖片旋轉處理
def rotate_image(image_path):
    image = Image.open(image_path)
    rotated_image = image.rotate(90)
    rotated_image_path = 'rotated_image.png'
    rotated_image.save(rotated_image_path)
    return rotated_image_path

# 圖片辨識
def image_recognition(image_path):
    # 在這裡實現與第三方圖片辨識服務的串接，可以使用相應的API或工具
    # 返回圖片辨識結果
    return '辨識結果'

# BOT啟動
bot.run('YOUR_DISCORD_BOT_TOKEN')

if __name__ == "__main__":
    bot.run('YOUR_DISCORD_BOT_TOKEN')
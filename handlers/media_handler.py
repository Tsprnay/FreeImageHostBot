# Author: https://github.com/Tsprnay
import os

from aiogram import Bot, types

from func.uploader import upload_image, random_string


async def media_handler(message: types.Message, bot: Bot):
    if message.video:
        await bot.send_message(message.from_user.id, "Our bot currently doesn't support video files.")
    elif message.photo:
        file_name = await random_string(18)
        file_id = message.photo[-1].file_id
        file_path = await bot.get_file(file_id)
        downloaded_file = await bot.download_file(file_path.file_path)
        with open("media/" + file_name + ".jpg", "wb") as f:
            f.write(downloaded_file.getvalue())
        image_url = await upload_image(open("media/" + file_name + ".jpg", "rb"))
        if image_url:
            await bot.send_message(message.from_user.id, f"Your image URL: {image_url}")
        os.remove("media/" + file_name + ".jpg")
    elif message.animation:
        await bot.send_message(message.from_user.id, "Our bot currently doesn't support GIF files.")
    else:
        await bot.send_message(message.from_user.id, "Currently, our bot does not support the type of files you send.")

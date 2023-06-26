# Author: https://github.com/Tsprnay
from aiogram import Bot, types

async def start_handler(message: types.Message, bot: Bot):
    await bot.send_message(message.from_user.id, "Welcome to the bot! Type /help to see the commands.")

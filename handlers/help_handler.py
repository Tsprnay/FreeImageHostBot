# Author: https://github.com/Tsprnay
from aiogram import Bot, types
async def help_handler(message: types.Message, bot: Bot):
    await bot.send_message(message.from_user.id, "To use our bot you just need send image.")

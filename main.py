import asyncio
import logging
import os

from aiogram import types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from func.config import bot, dp
from handlers.help_handler import help_handler
from handlers.media_handler import media_handler
from handlers.start_handler import start_handler

logging.basicConfig(level=logging.INFO)

async def main():
    if os.path.exists('media') == False:
        os.mkdir('media')
    @dp.message_handler(commands=["start"])
    async def wrapper(message: types.Message):
        await start_handler(message, bot)
    @dp.message_handler(commands=["help"])
    async def wrapper(message: types.Message):
        await help_handler(message, bot)
    @dp.message_handler(content_types=[types.ContentType.PHOTO, types.ContentType.VIDEO, types.ContentType.ANIMATION])
    async def wrapper(message: types.Message):
        await media_handler(message, bot)




if __name__ == "__main__":
    try:
        asyncio.run(main())
        dp.middleware.setup(LoggingMiddleware())
        asyncio.run(dp.start_polling())
    except KeyboardInterrupt:
        logging.info("Боты остановлены")

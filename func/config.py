# Author: https://github.com/Tsprnay
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

token = os.getenv('TOKEN')
freeimageapi = os.getenv('FreeImage_API')

bot = Bot(token=token)
dp = Dispatcher(bot)

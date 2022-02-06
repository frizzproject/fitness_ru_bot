from aiogram import Bot, Dispatcher
from storage import storage
import cfg

# Init
bot = Bot(token = cfg.API_TOKEN)
dp = Dispatcher(bot, storage = storage)
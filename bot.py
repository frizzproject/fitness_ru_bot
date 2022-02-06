from aiogram import executor
from dispatcher import dp
import logging
import handlers

# Logging
logging.basicConfig(level = logging.INFO)

# Lunch bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)

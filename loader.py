import logging

from aiogram import Bot, Dispatcher
from aiogram.utils.i18n.core import I18n
from data import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

i18n: I18n = I18n(path="locales", default_locale="en", domain="bot")

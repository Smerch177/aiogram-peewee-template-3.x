from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat, BotCommand

from bot.middlewares import i18n
from loader import bot
from aiogram.utils.i18n import gettext as _


def get_default_commands(lang: str = 'en') -> list[BotCommand]:
    return [
        BotCommand(command='/start', description=_('start bot', locale=lang)),
        BotCommand(command='/help', description=_('how it works?', locale=lang)),
        BotCommand(command='/lang', description=_('change language', locale=lang)),
        BotCommand(command='/settings', description=_('open bot settings', locale=lang)),
    ]


async def set_default_commands():
    await bot.set_my_commands(commands=get_default_commands(), scope=BotCommandScopeDefault())

    for lang in i18n.available_locales:
        await bot.set_my_commands(commands=get_default_commands(lang), scope=BotCommandScopeDefault(),
                                  language_code=lang)


async def set_user_commands(user_id: int, commands_lang: str):
    await bot.set_my_commands(commands=get_default_commands(commands_lang), scope=BotCommandScopeChat(chat_id=user_id))

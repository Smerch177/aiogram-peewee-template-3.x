from aiogram.types import BotCommandScopeChat, BotCommand

from loader import bot
from .default import get_default_commands
from aiogram.utils.i18n import gettext as _


def get_admin_commands(lang: str = 'en') -> list[BotCommand]:
    commands = get_default_commands(lang)

    commands.extend([
        BotCommand(command='/export_users', description=_('export users to csv', locale=lang)),
        BotCommand(command='/count_users', description=_('count users who contacted the bot', locale=lang)),
        BotCommand(command='/count_active_users',
                   description=_('count active users (who didn\'t block the bot)', locale=lang)),
    ])

    return commands


async def set_admin_commands(user_id: int, commands_lang: str):
    await bot.set_my_commands(commands=get_admin_commands(commands_lang), scope=BotCommandScopeChat(chat_id=user_id))

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from bot.commands import get_admin_commands, get_default_commands, set_admin_commands
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.keyboards.inline import get_language_inline_markup
from models import User

router = Router()


@router.message(CommandStart())
async def _start(message: Message, user: User):
    if user.is_admin:
        await set_admin_commands(user.id, user.language)
    text = _('Hi {full_name}!\n'
             'Choose your language').format(full_name=user.name)
    await message.answer(text, reply_markup=get_language_inline_markup())


@router.message(F.text == __('Help 🆘'))
@router.message(Command('help'))
async def _help(message: Message, user: User):
    commands = get_admin_commands(user.language) if user.is_admin else get_default_commands(
        user.language_code)

    text = _('Help 🆘') + '\n\n'
    for command in commands:
        text += f'{command.command} - {_(command.description)}\n'

    await message.answer(text)

from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types import Message

from bot.factory.callbacks import LanguageCallbackFactory
from bot.commands import set_admin_commands, set_user_commands

from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.keyboards.default import get_default_markup
from bot.keyboards.inline import get_language_inline_markup
from bot.middlewares.i18n import language_middleware
from models import User

router = Router()


@router.callback_query(LanguageCallbackFactory.filter())
async def _change_language(callback: types.CallbackQuery, callback_data: LanguageCallbackFactory, user: User):
    language_code = callback_data.language_code
    await language_middleware.set_locale(callback.from_user, language_code)

    if user.is_admin:
        await set_admin_commands(user.id, language_code)
    else:
        await set_user_commands(user.id, language_code)

    await callback.message.answer(_('Language changed successfully\n'
                                    'Press /help to find out how I can help you'),
                                  reply_markup=get_default_markup(user))
    await callback.message.delete()


@router.message(F.text == __('Settings 🛠'))
@router.message(Command(commands=['lang', 'settings']))
async def _settings(message: Message):
    text = _('Choose your language')

    await message.answer(text, reply_markup=get_language_inline_markup())

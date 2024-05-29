from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.types import Message

from bot.keyboards.default import get_default_markup
from models import User
from aiogram.utils.i18n import gettext as _


router = Router()


@router.message(StateFilter('*'))
async def _default_menu(message: Message, user: User):
    await message.answer(_('Choose an action from the menu 👇'), reply_markup=get_default_markup(user))

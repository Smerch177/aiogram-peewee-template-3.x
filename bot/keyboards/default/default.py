from aiogram.types import ReplyKeyboardRemove, KeyboardButton

from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_default_markup(user):
    builder = ReplyKeyboardBuilder()

    builder.add(KeyboardButton(text=_('Help 🆘')), KeyboardButton(text=_('Settings 🛠')))

    if user.is_admin:
        builder.add(KeyboardButton(text=_('Export users 📁')))
        builder.add(KeyboardButton(text=_('Count users 👥')))
        builder.add(KeyboardButton(text=_('Count active users 👥')))

    if len(builder._markup) < 1:
        return ReplyKeyboardRemove()

    builder.adjust(3)

    return builder.as_markup()

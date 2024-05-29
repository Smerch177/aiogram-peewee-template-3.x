from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.factory.callbacks import LanguageCallbackFactory


def get_language_inline_markup():
    builder = InlineKeyboardBuilder()
    builder.button(text="🇺🇸 English", callback_data=LanguageCallbackFactory(language_code="en")),
    builder.button(text="🏳️ Русский", callback_data=LanguageCallbackFactory(language_code="ru")),
    builder.button(text='🇺🇦 Українська', callback_data=LanguageCallbackFactory(language_code='uk'))
    return builder.as_markup()

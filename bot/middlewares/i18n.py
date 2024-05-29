"""
- Собираем все текста с проекта
pybabel extract --input-dirs=. -o locales/bot.pot --project=bot

- Создаем файлы с переводами на разные языки
pybabel init -i locales/bot.pot -d locales -D bot -l en
pybabel init -i locales/bot.pot -d locales -D bot -l ru
pybabel init -i locales/bot.pot -d locales -D bot -l uk

- После того как все текста переведены, нужно скомпилировать все переводы
pybabel compile -d locales -D bot --statistics

pybabel update -i locales/bot.pot -d locales -D bot

"""
from typing import Any

from aiogram.types import CallbackQuery, Message, InlineQuery, User, TelegramObject
from aiogram.utils.i18n import SimpleI18nMiddleware

from bot.database.services import edit_user_language

from loader import i18n as _i18n


class ACLMiddleware(SimpleI18nMiddleware):
    current_locale = "en"

    async def get_locale(self, event: TelegramObject, data: dict[str, Any]) -> str:
        if not isinstance(event, (Message, CallbackQuery, InlineQuery)):
            return self.current_locale

        user = data['user']

        return user.language or self.current_locale

    async def set_locale(self, user: User, language_code: str) -> None:
        await edit_user_language(user, language_code)
        self.i18n.current_locale = language_code


language_middleware = ACLMiddleware(i18n=_i18n)

import contextlib
import csv

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.database.services import count_users, get_users
from bot.filters.admin import AdminFilter
from loader import bot, config

router = Router()


@router.message(F.text == __('Export users 📁'), AdminFilter())
@router.message(Command('export_users'), AdminFilter())
async def _export_users(message: Message):
    count = await count_users()

    file_path = config.DIR / 'users.csv'
    with open(file_path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(['id', 'name', 'username', 'language', 'created_at'])

        for user in await get_users():
            writer.writerow([user.id, user.name, user.username, user.language, user.created_at])

    text_file = FSInputFile(file_path, filename='users.csv')
    await message.answer_document(text_file, caption=_('Total users: {count}').format(count=count))


@router.message(F.text == __('Count users 👥'), AdminFilter())
@router.message(Command('count_users'), AdminFilter())
async def _users_count(message: Message):
    count = await count_users()

    await message.answer(_('Total users: {count}').format(count=count))


@router.message(F.text == __('Count active users 👥'), AdminFilter())
@router.message(Command('count_active_users'), AdminFilter())
async def _active_users_count(message: Message):
    users = await get_users()

    count = 0
    for user in users:
        with contextlib.suppress(Exception):
            if await bot.send_chat_action(user.id, 'typing'):
                count += 1
    await message.answer(_('Active users: {count}').format(count=count))

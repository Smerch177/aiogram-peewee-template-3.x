from aiogram.filters import BaseFilter
from aiogram.types import Message

from models import User


class AdminFilter(BaseFilter):
    """Allows only administrators (whose database column is_admin=True)."""

    async def __call__(self, message: Message, user: User) -> bool:
        return user.is_admin if message.from_user else False

from peewee import fn, DoesNotExist

from bot.database.main import objects
from data.config import ADMINS
from models import User
from utils.misc.logging import logger


async def count_users() -> int:
    return await objects.scalar(User.select(fn.COUNT(User.id)))


async def get_users() -> list[User]:
    query = await objects.execute(User.select())

    return list(query)


async def get_user(id: int) -> User | None:
    try:
        return await objects.get(User, id=id)
    except DoesNotExist:
        return None


async def update_user(user: User, name: str, username: str = None) -> User:
    user.name = name
    user.username = username
    await objects.update(user)

    return user


async def edit_user_language(user: User, language: str):
    user = await get_user(user.id)
    user.language = language
    await objects.update(user)


async def create_user(id: int, name: str, username: str = None, language: str = None) -> User:
    is_admin = str(id) in ADMINS
    new_user = await objects.create(User, id=id, name=name, username=username, language=language, is_admin=is_admin)

    logger.info(f'New user {new_user}')

    return new_user


async def get_or_create_user(id: int, name: str, username: str = None, language: str = None) -> User:
    user = await get_user(id)

    if user:
        user = await update_user(user, name, username)

        return user

    user = await create_user(id, name, username, language)

    return user

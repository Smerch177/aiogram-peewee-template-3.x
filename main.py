import asyncio
from peewee import PostgresqlDatabase, SqliteDatabase

from bot.handlers import get_handlers_router
from bot.middlewares import register_middlewares

from data import config
from loader import dp, bot

if config.DB_USER and config.DB_PASSWORD and config.DB_HOST and config.DB_PORT and config.DB_NAME:
    database = PostgresqlDatabase(config.DB_NAME, user=config.DB_USER, password=config.DB_PASSWORD,
                                  host=config.DB_HOST, port=config.DB_PORT)
else:
    database = SqliteDatabase(f'{config.DIR}/database.sqlite3')


# Запуск бота
async def main():
    dp.include_router(get_handlers_router())
    register_middlewares(dp)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())


from aiogram import Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware


def register_middlewares(dp: Dispatcher) -> None:
    from .user import UsersMiddleware
    from .logging import LoggingMiddleware
    from .throttling import ThrottlingMiddleware
    from .i18n import language_middleware

    dp.message.outer_middleware(ThrottlingMiddleware())

    dp.update.outer_middleware(LoggingMiddleware())

    # dp.message.middleware(UsersMiddleware())
    # dp.callback_query.middleware(UsersMiddleware())
    # dp.inline_query.middleware(UsersMiddleware())
    UsersMiddleware().setup(dp)

    language_middleware.setup(dp)
    # dp.message.middleware(language_middleware)
    # dp.callback_query.middleware(language_middleware)
    # dp.inline_query.middleware(language_middleware)

    dp.callback_query.middleware(CallbackAnswerMiddleware())

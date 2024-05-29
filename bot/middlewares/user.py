from typing import Any, Awaitable, Callable, Optional, Set

from aiogram import BaseMiddleware, Router
from aiogram.dispatcher.event.bases import CancelHandler
from aiogram.types import Message, CallbackQuery, InlineQuery

from bot.database.services import get_or_create_user


class UsersMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery | InlineQuery,
            data: dict[str, Any],
    ) -> Any:
        if not isinstance(event, Message | CallbackQuery | InlineQuery):
            return await handler(event, data)

        if isinstance(event, Message) and (event.chat.type != 'private'):
            raise CancelHandler()

        message: Message | CallbackQuery | InlineQuery = event
        user = message.from_user

        if not user:
            return await handler(event, data)

        data['user'] = await get_or_create_user(user.id, user.full_name, user.username, user.language_code)

        return await handler(event, data)

    def setup(
        self: BaseMiddleware, router: Router, exclude: Optional[Set[str]] = None
    ) -> BaseMiddleware:
        """
        Register middleware for all events in the Router

        :param router:
        :param exclude:
        :return:
        """
        if exclude is None:
            exclude = set()
        exclude_events = {"update", *exclude}
        for event_name, observer in router.observers.items():
            if event_name in exclude_events:
                continue
            observer.outer_middleware(self)
        return self

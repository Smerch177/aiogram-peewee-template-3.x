from aiogram import Router


def get_handlers_router() -> Router:
    from . import start, settings, helpers, admin_menu
    router = Router()
    router.include_router(start.router)
    router.include_router(settings.router)
    router.include_router(admin_menu.router)

    # last router because helpers.router is handling all messages
    router.include_router(helpers.router)

    return router

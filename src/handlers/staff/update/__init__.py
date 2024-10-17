from aiogram import Router

from . import ban_or_unban

__all__ = ('router',)

router = Router(name=__name__)
router.include_router(ban_or_unban.router)
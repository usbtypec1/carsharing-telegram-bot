from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery
from fast_depends import inject, Depends

from callback_data import StaffUpdateCallbackData
from dependencies.repositories import get_staff_repository
from enums import StaffUpdateAction
from repositories import StaffRepository
from views.base import edit_message_by_view
from views.staff import StaffDetailView

__all__ = ('router',)

router = Router(name=__name__)


@router.callback_query(
    StaffUpdateCallbackData.filter(
        rule=F.action.in_({StaffUpdateAction.BAN, StaffUpdateAction.UNBAN}),
    ),
    StateFilter('*'),
)
@inject
async def on_ban_or_unban_staff(
        callback_query: CallbackQuery,
        callback_data: StaffUpdateCallbackData,
        staff_repository: StaffRepository = Depends(
            dependency=get_staff_repository,
            use_cache=False,
        ),
) -> None:
    if callback_data.action == StaffUpdateAction.BAN:
        await staff_repository.update_by_telegram_id(
            telegram_id=callback_data.telegram_id,
            is_banned=True,
        )
    else:
        await staff_repository.update_by_telegram_id(
            telegram_id=callback_data.telegram_id,
            is_banned=False,
        )
    staff = await staff_repository.get_user_by_id(callback_data.telegram_id)
    view = StaffDetailView(staff)
    await edit_message_by_view(callback_query.message, view)
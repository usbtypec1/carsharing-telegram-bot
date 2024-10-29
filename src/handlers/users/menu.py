from aiogram import Router
from aiogram.filters import StateFilter, CommandStart, ExceptionTypeFilter, \
    invert_f
from aiogram.types import Message, ErrorEvent
from fast_depends import Depends, inject

from dependencies.repositories import get_staff_repository, get_shift_repository
from exceptions import StaffNotFoundError, StaffHasNoActiveShiftError
from filters import admins_filter
from repositories import StaffRepository, ShiftRepository
from views.admins import AdminMenuView
from views.base import answer_view
from views.menu import MainMenuView, RegisterView, StaffShiftCarWashMenuView

__all__ = ('router',)

router = Router(name=__name__)


@router.error(ExceptionTypeFilter(StaffNotFoundError))
async def on_performer_not_found_error(event: ErrorEvent) -> None:
    view = RegisterView()
    if event.update.message is not None:
        await answer_view(event.update.message, view)
    elif event.update.callback_query is not None:
        await answer_view(event.update.callback_query.message, view)
    else:
        raise event.exception


@router.message(
    CommandStart(),
    invert_f(admins_filter),
    StateFilter('*'),
)
@inject
async def on_show_menu(
        message: Message,
        staff_repository: StaffRepository = Depends(
            get_staff_repository,
            use_cache=False,
        ),
        shift_repository: ShiftRepository = Depends(
            get_shift_repository,
            use_cache=False,
        ),
) -> None:
    staff = await staff_repository.get_by_id(message.from_user.id)
    try:
        await shift_repository.get_active(message.from_user.id)
    except StaffHasNoActiveShiftError:
        view = StaffShiftCarWashMenuView()
    else:
        view = MainMenuView()
    await answer_view(message, view)


@router.message(
    CommandStart(),
    admins_filter,
    StateFilter('*'),
)
@inject
async def on_show_admin_menu(
        message: Message,
) -> None:
    view = AdminMenuView()
    await answer_view(message, view)

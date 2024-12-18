from aiogram.filters.callback_data import CallbackData

from callback_data.prefixes import CallbackDataPrefix
from enums import StaffUpdateAction

__all__ = (
    'StaffDetailCallbackData',
    'StaffUpdateCallbackData',
)


class StaffDetailCallbackData(
    CallbackData,
    prefix=CallbackDataPrefix.STAFF_DETAIL,
):
    telegram_id: int


class StaffUpdateCallbackData(
    CallbackData,
    prefix=CallbackDataPrefix.STAFF_UPDATE,
):
    telegram_id: int
    action: StaffUpdateAction

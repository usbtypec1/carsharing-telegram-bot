from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import Message

from config import Config
from filters import admins_filter
from ui.views import AdminOtherMenuView
from ui.views import answer_text_view
from ui.views import ButtonText
from ui.views import ReportsMenuView

__all__ = ('router',)

router = Router(name=__name__)


@router.message(
    F.text == ButtonText.OTHER,
    admins_filter,
    StateFilter('*'),
)
async def on_other(
        message: Message,
        config: Config,
) -> None:
    view = AdminOtherMenuView(config.web_app_base_url)
    await answer_text_view(message, view)


@router.message(
    F.text == ButtonText.REPORTS,
    admins_filter,
    StateFilter('*'),
)
async def on_show_reports(message: Message, config: Config) -> None:
    view = ReportsMenuView(
        staff_revenue_report_table_url=config.staff_revenue_report_table_url,
        service_costs_report_table_url=config.service_costs_report_table_url,
    )
    await answer_text_view(message, view)

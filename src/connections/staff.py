from collections.abc import Iterable

import httpx

from connections.base import ApiConnection
from logger import create_logger

__all__ = ('StaffConnection',)

from models import MonthAndYear

logger = create_logger('connections')


class StaffConnection(ApiConnection):

    async def get_by_id(self, user_id: int) -> httpx.Response:
        url = f'/staff/{user_id}/'
        return await self._http_client.get(url)

    async def create(
            self,
            telegram_id: int,
            full_name: str,
            car_sharing_phone_number: str,
            console_phone_number: str,
    ) -> httpx.Response:
        url = '/staff/'
        request_data = {
            'id': telegram_id,
            'full_name': full_name,
            'car_sharing_phone_number': car_sharing_phone_number,
            'console_phone_number': console_phone_number,
        }
        response = await self._http_client.post(url, json=request_data)
        logger.debug(
            'Retrieved staff create response',
            extra={
                'status_code': response.status_code,
                'body': response.text,
            },
        )
        return response

    async def get_all(self) -> httpx.Response:
        url = '/staff/'
        return await self._http_client.get(url)

    async def update_by_telegram_id(
            self,
            *,
            telegram_id: int,
            is_banned: bool,
    ) -> httpx.Response:
        url = f'/staff/{telegram_id}/'
        request_data = {'is_banned': is_banned}
        return await self._http_client.put(url, json=request_data)

    async def update_available_dates(
            self,
            *,
            staff_id: int,
            months_and_years: Iterable[dict],
    ) -> httpx.Response:
        url = f'/staff/{staff_id}/available-dates/'
        request_data = {'dates': months_and_years}
        return await self._http_client.patch(url, json=request_data)

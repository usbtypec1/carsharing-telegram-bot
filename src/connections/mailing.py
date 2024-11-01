from collections.abc import Iterable

import httpx

from connections.base import ApiConnection
from logger import create_logger
from models import Button

__all__ = ('MailingConnection',)

logger = create_logger('connections')


class MailingConnection(ApiConnection):

    async def send_to_all(
            self,
            *,
            text: str,
            reply_markup: Iterable[Iterable[Button]] | None = None,
    ) -> httpx.Response:
        url = '/mailing/all/'
        request_data = {'text': text}
        if reply_markup is not None:
            request_data['reply_markup'] = reply_markup
        logger.debug(
            'Creating mailing to all users',
            extra={'request_data': request_data},
        )
        response = await self._http_client.post(url, json=request_data)
        logger.debug(
            'Mailing to all users created',
            extra={'status_code': response.status_code},
        )
        return response

    async def send_to_specific_staff(
            self,
            *,
            text: str,
            chat_ids: Iterable[int],
            reply_markup: Iterable[Iterable[Button]] | None = None,
    ) -> httpx.Response:
        url = '/mailing/staff/'
        request_data = {
            'text': text,
            'chat_ids': chat_ids,
        }
        if reply_markup is not None:
            request_data['reply_markup'] = reply_markup
        logger.debug(
            'Creating mailing to specific staff',
            extra={'request_data': request_data},
        )
        response = await self._http_client.post(url, json=request_data)
        logger.debug(
            'Mailing to specific staff created',
            extra={'status_code': response.status_code},
        )
        return response

    async def send_to_last_active_staff(
            self,
            *,
            text: str,
            last_days: int,
            reply_markup: Iterable[Iterable[Button]] | None = None,
    ) -> httpx.Response:
        url = '/mailing/last-active/'
        request_data = {
            'text': text,
            'last_days': last_days,
        }
        if reply_markup is not None:
            request_data['reply_markup'] = reply_markup
        logger.debug(
            'Creating mailing to last active staff',
            extra={'request_data': request_data},
        )
        response = await self._http_client.post(url, json=request_data)
        logger.debug(
            'Mailing to last active staff created',
            extra={'status_code': response.status_code},
        )
        return response

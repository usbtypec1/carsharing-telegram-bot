import httpx

from connections.base import ApiConnection
from logger import create_logger
from models import CarToWash

__all__ = ('CarToWashConnection',)

logger = create_logger('connections')


class CarToWashConnection(ApiConnection):

    async def create(
            self,
            car_to_wash: CarToWash,
    ) -> httpx.Response:
        url = '/shifts/cars/'
        request_data = car_to_wash.model_dump()
        logger.debug(
            'Adding car to wash',
            extra={'request_data': request_data}
        )
        response = await self._http_client.post(url, json=request_data)
        logger.debug(
            'Car to wash created',
            extra={'status_code': response.status_code}
        )
        return response

    async def get_all(self, staff_id: int) -> httpx.Response:
        url = f'/shifts/cars/staff/{staff_id}/'
        logger.debug(
            'Retrieving all cars added in shift',
            extra={'staff_id': staff_id},
        )
        response = await self._http_client.get(url)
        logger.debug(
            'Retrieved all cars added in shift',
            extra={'status_code': response.status_code},
        )
        return response
import datetime

from pydantic import BaseModel

from enums import CarClass, WashType

__all__ = (
    'CarToWash',
    'AdditionalService',
    'Car',
    'CarAdditionalServices',
    'ShiftCarsCountByStaff',
    'CarStatisticsItem',
    'ShiftCarsWithoutWindshieldWasher',
)


class AdditionalService(BaseModel):
    name: str
    count: int


class CarToWash(BaseModel):
    number: str
    class_type: CarClass
    wash_type: WashType
    windshield_washer_refilled_bottle_percentage: int
    additional_services: list[AdditionalService]


class Car(BaseModel):
    id: int
    number: str
    car_class: CarClass
    wash_type: WashType
    windshield_washer_refilled_bottle_percentage: int
    created_at: datetime.datetime
    additional_services: list[AdditionalService]


class CarAdditionalServices(BaseModel):
    car_id: int
    additional_services: list[AdditionalService]


class CarStatisticsItem(BaseModel):
    staff_id: int
    staff_full_name: str
    cars_count: int


class ShiftCarsCountByStaff(BaseModel):
    date: datetime.date
    cars: list[CarStatisticsItem]


class ShiftCarsWithoutWindshieldWasher(BaseModel):
    date: datetime.date
    cars: list[str]

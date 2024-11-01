from enum import StrEnum

__all__ = ('ButtonText',)


class ButtonText(StrEnum):
    STAFF_LIST = '👥 Список всех сотрудников'
    SHIFTS = '📅 Графики'
    REPORTS = '📊 Отчеты'
    SHIFTS_TODAY = '📅 Сегодня в смене'
    CAR_WASH_LIST = '🚿 Меню моек'
    PENALTY = '🛑 Штрафануть'
    SURCHARGE = '💰 Доплатить'
    SHIFT_CARS_COUNT_BY_STAFF = '📊 Кто сколько'
    SHIFT_CARS_WITHOUT_WINDSHIELD_WASHER = '💧 Недоливы'
    MAILING = '📩 Рассылка'
    SHIFT_START = '🚀 Начать смену'
    SHIFT_START_EXTRA = '🚀 Начать доп.смену'
    SHIFT_SCHEDULE = '📅 График работы'
    REPORT_FOR_PERIOD = '📊 Отчет за период'
    SHIFT_ADD_CAR = '🚗 Добавить автомобиль'
    SHIFT_ADDITIONAL_SERVICES = '🔧 Отметить доп.услуги'
    SHIFT_ADDED_CARS = '🚗 Добавленные автомобили'
    SHIFT_CHANGE_CAR_WASH = '🫧 Поменять мойку'
    SHIFT_END = '🛑 Завершить смену'
    ATTACH_REPLY_MARKUP = '⌨ Привязать кнопки'
    SKIP = '➡ Пропустить'
    MAILING_STAFF = '👥 Выбрать сотрудников'
    REGISTER = '🚀 Зарегистрироваться'
    AVAILABLE_DATES = '📅 Месяцы отображения'
    MAIN_MENU = '📲 Главное меню'
    SCHEDULE_SELF = '📆 Мой график'
    CAR_ADDITIONAL_SERVICES = '🔧 Отметить доп.услуги авто'

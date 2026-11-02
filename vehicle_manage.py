from functools import wraps


def validate_fuel_consumption(method):
    """
    Декоратор для проверки условий перед расчётом расхода топлива.

    Что делает:
    1. Проверяет, что входной параметр (расстояние/время) неотрицателен.
    2. Вызывает декорируемый метод ровно один раз, чтобы получить расчётный
    расход.
    3. Проверяет, хватает ли топлива в баке на этот расход.
    4. Если всё ок — вычитает топливо из текущего уровня и возвращает расход.
    5. При любой ошибке — печатает сообщение и возвращает None.

    Важно: декоратор универсален и работает для Car, Airplane, Boat.
    """
    # Сохраняет имя и документацию оригинального метода (удобно для отладки)
    @wraps(method)
    def wrapper(self, value, *args, **kwargs):
        # Шаг 1: проверка на отрицательное значение
        # (расстояние или время не могут быть < 0)
        if value < 0:
            print("Ошибка: значение не может быть отрицательным.")
            return None

        # Шаг 2: вызываем метод расчёта расхода ровно один раз.
        # Передаём все аргументы, чтобы сигнатура оставалась гибкой.
        consumption = method(self, value, *args, **kwargs)

        # Если сам метод вернул None (внутренняя ошибка), дальше не идём.
        if consumption is None:
            return None

        # Шаг 3: проверка достаточности топлива.
        # Сравниваем требуемый расход с текущим уровнем в баке.
        if consumption > self._current_fuel_level:
            print(
                f"Ошибка: недостаточно топлива для поездки. "
                f"Нужно {consumption:.2f} л, "
                f"в наличии {self._current_fuel_level:.2f} л."
            )
            return None

        # Шаг 4: если всё ок, списываем топливо из бака.
        self._current_fuel_level -= consumption

        # Возвращаем именно РАСХОД (сколько потратили), а не остаток.
        return consumption

    return wrapper


class Vehicle:
    """
    Базовый класс для транспортных средств.
    Реализует общую логику: хранение имени, бака, текущего уровня топлива,
    а также методы заправки и вывода информации.
    """

    def __init__(self, name: str, fuel_tank_capacity: float):
        self._name = name
        self._fuel_tank_capacity = fuel_tank_capacity
        # При создании бак заполняется полностью
        self._current_fuel_level = fuel_tank_capacity

    def refuel(self, amount: float) -> None:
        """
        Заправка транспортного средства.
        Проверки:
        - amount должен быть положительным.
        - нельзя превысить вместимость бака.
        """
        if amount <= 0:
            print("Ошибка: количество топлива должно быть положительным.")
            return

        if amount + self._current_fuel_level > self._fuel_tank_capacity:
            print("Ошибка: превышение вместимости топливного бака.")
            return

        self._current_fuel_level += amount
        print(f"Заправлено {amount} л. "
              f"Текущий уровень: {self._current_fuel_level} л.")

    def display_info(self) -> None:
        """Отображает основную информацию о транспортном средстве."""
        print(
            f"Название: {self._name}, "
            f"Вместимость бака: {self._fuel_tank_capacity} л, "
            f"Текущий уровень топлива: {self._current_fuel_level} л."
        )


class Car(Vehicle):
    """
    Класс для представления автомобиля.
    Наследует от Vehicle.
    Специфика: расход топлива задаётся в литрах на 100 км.
    """

    def __init__(
        self,
        name: str,
        fuel_tank_capacity: float,
        fuel_consumption_per_100km: float
    ):
        super().__init__(name, fuel_tank_capacity)
        # Защищённый атрибут: расход в литрах на 100 км
        self._fuel_consumption_per_100km = fuel_consumption_per_100km

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, distance: float) -> float | None:
        """
        Рассчитать расход топлива для поездки на автомобиле.
        Формула: (расстояние / 100) * расход на 100 км.
        Декоратор validate_fuel_consumption берёт на себя проверки
        и списание топлива.
        """
        consumption = (distance / 100.0) * self._fuel_consumption_per_100km
        print(f"Расход на {distance} км: {consumption:.2f} л.")
        return consumption


class Airplane(Vehicle):
    """
    Класс для представления самолёта.
    Наследует от Vehicle.
    Специфика: расход топлива задаётся в литрах в час.
    """

    def __init__(
        self,
        name: str,
        fuel_tank_capacity: float,
        fuel_consumption_per_hour: float
    ):
        super().__init__(name, fuel_tank_capacity)
        # Защищённый атрибут: расход в литрах в час
        self._fuel_consumption_per_hour = fuel_consumption_per_hour

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, flight_time: float) -> float | None:
        """
        Рассчитать расход топлива для полёта.
        Формула: время полёта * расход в час.
        Проверки и списание топлива выполняет декоратор.
        """
        consumption = flight_time * self._fuel_consumption_per_hour
        print(f"Расход за {flight_time} ч: {consumption:.2f} л.")
        return consumption


class Boat(Vehicle):
    """
    Класс для представления катера.
    Наследует от Vehicle.
    Специфика: расход топлива задаётся в литрах в час (аналогично самолёту).
    """

    def __init__(
        self,
        name: str,
        fuel_tank_capacity: float,
        fuel_consumption_per_hour: float
    ):
        super().__init__(name, fuel_tank_capacity)
        # Защищённый атрибут: расход в литрах в час
        self._fuel_consumption_per_hour = fuel_consumption_per_hour

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, travel_time: float) -> float | None:
        """
        Рассчитать расход топлива для путешествия на катере.
        Формула: время в пути * расход в час.
        Проверки и списание топлива выполняет декоратор.
        """
        consumption = travel_time * self._fuel_consumption_per_hour
        print(f"Расход за {travel_time} ч: {consumption:.2f} л.")
        return consumption


# Создание объектов
car = Car("Toyota Camry", 60, 8)
airplane = Airplane("Boeing 737", 20000, 2500)
boat = Boat("Sea Ray", 150, 30)

# Отображение информации
# Название: Toyota Camry, Вместимость бака: 60 л,
# Текущий уровень топлива: 60 л.
car.display_info()
# Название: Boeing 737, Вместимость бака: 20000 л,
# Текущий уровень топлива: 20000 л.
airplane.display_info()
# Название: Sea Ray, Вместимость бака: 150 л, Текущий уровень топлива: 150 л.
boat.display_info()

# Заправка транспортных средств
car.refuel(30)  # Ошибка: превышение вместимости топливного бака.
airplane.refuel(10000)  # Ошибка: превышение вместимости топливного бака.
boat.refuel(80)  # Ошибка: превышение вместимости топливного бака.

# Расчёт расхода топлива
car.calculate_fuel_consumption(150)  # Расход на 150 км: 12.00 л.
airplane.calculate_fuel_consumption(3)  # Расход за 3 ч: 7500.00 л.
boat.calculate_fuel_consumption(2)  # Расход за 2 ч: 60.00 л.

def validate_fuel_consumption(method):
    """
    Декоратор для проверки условий перед расчётом расхода топлива.
    Проверяет, что время или расстояние неотрицательны и достаточно топлива.
    """
    def wrapper(self, value):
        # вызов метода: method(self, value)
        pass
    return wrapper


class Vehicle:
    """
    Базовый класс для транспортных средств.
    """
    def __init__(self, name: str, fuel_tank_capacity: float):
        self._name = name
        self._fuel_tank_capacity = fuel_tank_capacity
        self._current_fuel_level = fuel_tank_capacity

    def refuel(self, amount: float) -> None:
        """
        Заправка транспортного средства.
        """
        if amount <= 0:
            print('Ошибка: количество топлива должно быть положительным.')
            return
        if amount + self._current_fuel_level > self._fuel_tank_capacity:
            print('Ошибка: превышение вместимости топливного бака.')
            return
        self._current_fuel_level += amount
        print(
            f'Заправлено {amount} л. '
            f'Текущий уровень: {self._current_fuel_level} л.'
        )

    def display_info(self) -> None:
        """Отображает основную информацию о транспортном средстве."""
        print(
            f'Название: {self._name}, '
            f'Вместимость бака: {self._fuel_tank_capacity} л, '
            f'Текущий уровень топлива: {self._current_fuel_level} л.'
        )


class Car(Vehicle):
    """
    Класс для представления автомобиля.
    Наследует от Vehicle.
    """
    def __init__(
            self, name: str,
            fuel_tank_capacity: float,
            fuel_consumption_per_100km: float
    ):
        super().__init__(name, fuel_tank_capacity)
        self._fuel_consumption_per_100km = fuel_consumption_per_100km

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, distance: float) -> float | None:
        """Рассчитать расход топлива для поездки."""
        consumption = (distance / 100.0) * self._fuel_consumptiom_per_100km
        print(f'Расход на {distance} км: {consumption:.2f} л.')
        return consumption


class Airplane(Vehicle):
    """
    Класс для представления самолёта.
    Наследует от Vehicle.
    """
    def __init__(
            self, name: str,
            fuel_tank_capacity: float,
            fuel_consumption_per_hour: float
    ):
        super().__init__(name, fuel_tank_capacity)
        self._fuel_consumption_per_hour = fuel_consumption_per_hour

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, flight_time: float) -> float | None:
        """Рассчитать расход топлива для полёта за заданное время."""
        consumption = flight_time * self._fuel_consumption_per_hour
        print(f'Расход за {flight_time} ч: {consumption:.2f} л.')
        return consumption


class Boat(Vehicle):
    """
    Класс для представления катера.
    Наследует от Vehicle.
    """
    def __init__(
            self, name: str,
            fuel_tank_capacity: float,
            fuel_consumption_per_hour: float
    ):
        super().__init__(name, fuel_tank_capacity)
        self._fuel_consumption_per_hour = fuel_consumption_per_hour

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, travel_time: float) -> float | None:
        """Рассчитать расход топлива для поездки."""
        consumption = travel_time * self._fuel_consumption_per_hour
        print(f'Расход за {travel_time} ч: {consumption:.2f} л.')
        return consumption


# Создание объектов
car = Car("Toyota Camry", 60, 8)
airplane = Airplane("Boeing 737", 20000, 2500)
boat = Boat("Sea Ray", 150, 30)

# Отображение информации
car.display_info() # Название: Toyota Camry, Вместимость бака: 60 л, Текущий уровень топлива: 60 л.
airplane.display_info() # Название: Boeing 737, Вместимость бака: 20000 л, Текущий уровень топлива: 20000 л.
boat.display_info() # Название: Sea Ray, Вместимость бака: 150 л, Текущий уровень топлива: 150 л.

# Заправка транспортных средств
car.refuel(30) # Ошибка: превышение вместимости топливного бака.
airplane.refuel(10000) # Ошибка: превышение вместимости топливного бака.
boat.refuel(80) # Ошибка: превышение вместимости топливного бака.

# Расчёт расхода топлива
car.calculate_fuel_consumption(150) # Расход на 150 км: 12.00 л.
airplane.calculate_fuel_consumption(3) # Расход за 3 ч: 7500.00 л.
boat.calculate_fuel_consumption(2) # Расход за 2 ч: 60.00 л.
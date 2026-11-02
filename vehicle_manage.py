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
    def __init__(self, name: str, fuel_tank_capacity: int):
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


class Car:
    """
    Класс для представления автомобиля.
    Наследует от Vehicle.
    """
    pass


class Airplane:
    """
    Класс для представления самолёта.
    Наследует от Vehicle.
    """
    pass


class Boat:
    """
    Класс для представления катера.
    Наследует от Vehicle.
    """
    pass


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
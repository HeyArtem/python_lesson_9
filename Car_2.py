# Я создал Car_2 т.к. нужно было  откорректировать Car

print()
print()
print('    - Импортирование модуля в модуль')

"""Класс для представления автомобиля.""" # Cтрока документации с кратким описанием; желат

class Car():
    """" Простая модель автомобиля. """

    def __init__(self, make, model, year):
        """" Инициализирует атрибуты описания автомобиля. """

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """" Возвращает аккуратно отформатированное описание. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """" Выводит пробег машины в километрах"""
        print(f" Этот автомобил имеет пробег {self.odometer_reading} километров")

    def update_odometer(self, mileage):
        """"
        Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки - изменение отклоняется
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(" Вы не можете откатить одометр")

    def increment_odometer(self, kilometers):
        """" Увеличивает показания одометра с заданным приращением. """
        if kilometers >= 0:
            self.odometer_reading += kilometers
        else:
            print(" Откатить одометр невозможно!!! ")
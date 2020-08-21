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







print()
print()
print('    Хранение нескольких классов в модуле')
""""
В одном модуле можно хранить сколько угодно классов, хотя все эти классы должны быть каким-то
образом связаны друг с другом.

Классы Battery и ElectricCar могут использоваться для представления электромобилей,
поэтому добавим их в модуль car.py:

Я перехожу на car.py

# добавить в конец файла car.py

"""

class Battery():
    """" Простая модель акб электромобиля. """

    def __init__(self, battery_size = 70):
        """" Инициализация атрибуирв акб. """
        self.battery_size = battery_size

    def describe_battery(self):
        """"Выводит информацию о мощности акб. """
        print(f" Этот автомобиль имеет акб мощностью {self.battery_size} kWh. ")

    def get_range(self):
        """"Выводит приблизительный запас хода для акб. """
        if self.battery_size == 70:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"Этот автомиль проедет {range} миль, до следующей зарядки")


class ElectricCar(Car):
    """" представляет аспекты машины, специфические для электромобилей. """
    def __init__(self, make, model, year):
        """"
        Инициализирует атрибуты класса-родителя.
         Затем инициализирует атрибуты, специфические для электромобиля.

        """
        super().__init__(make, model, year)
        self.battery = Battery()
# Создадим новую программу, куда импортируем класс ElectricCar и создать новый экземпляр
# электромобиля:
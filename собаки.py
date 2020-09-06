# Сравнить экземпляры собак по возрасту

class Dog():  # определяется класс с именем Dog
    """Простая модель собаки."""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(f"{self.name} rolled over!")



    def compare(self): # метод сравнения
        if d1.age < d2.age:
            print('Экземпляр d2 старше!')
        elif d1.age > d2.age:
            print('Экземпляр d1 старше!')
        else:
            print('Данные экземпляры погодки!')

d1 = Dog('Katty', 7)
d2 = Dog('Fred', 6)

print(d1.compare()) #  почему то None выводится

print(f"Экземпляру d1 {d1.age} лет, а экземпляру d2 {d2.age} лет")



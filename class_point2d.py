# Создаю на уроке с проподователем
class Point2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x**2 + self.y**2)**0.5 # расстояние до центра координат

p = Point2D(2,3)

print(p, type(p))
print('Выведем координаты: ', p.x, p.y)
print(p.distance())


print()
print('Усовершенствуем')

class Point2D():

    def __init__(self, x, y): # Инициализация
        self.x = x
        self.y = y

    def __str__(self):        # Вывод
        return f"Точка ({self.x}, {self.y})"

    def distance(self):
        return (self.x**2 + self.y**2)**0.5 # расстояние до центра координат

p = Point2D(2,3)


print('Выведем координаты: ', p.x, p.y)
print(p)
print(p.distance())

print()
print('   Теперь создадим метод поиска расстояния до другой точки')

class Point2D():

    def __init__(self, x, y): # Инициализация
        self.x = x
        self.y = y

    def __str__(self):        # Вывод
        return f"Точка ({self.x}, {self.y})"

    def distance(self):
        return (self.x**2 + self.y**2)**0.5 # расстояние до центра координат

    def point_distance(self, a, b):
        return ((self.x-a)**2 + (self.y-b)**2)**0.5


p = Point2D(2,3)

print('Выведем координаты: ', p.x, p.y)
print(p)
print(p.distance())
print(p.point_distance(3,4))




print()
print('   Перегрузка операция сложение')

class Point2D():

    def __init__(self, x, y): # Инициализация
        self.x = x
        self.y = y

    def __str__(self):        # Вывод
        return f"Точка ({self.x}, {self.y})"


    def __add__(self, other):                          # Перегрузка плюсом
        return Point2D(self.x + other.x, self.y + other.y)



    def distance(self):
        return (self.x**2 + self.y**2)**0.5 # расстояние до центра координат

    def point_distance(self, a, b):
        return ((self.x-a)**2 + (self.y-b)**2)**0.5


p = Point2D(2, 3)
q = Point2D(3,-2)

print(p+q)

print('Выведем координаты: ', p.x, p.y)
print(p)
print(p.distance())
print(p.point_distance(3,4))

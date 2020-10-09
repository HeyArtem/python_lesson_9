

print('    -1. Создайте класс с именем Restaurant.')
''''
1. Создайте класс с именем Restaurant.
Метод __init__() класса Restaurant должен содержать два атрибута:
restaurant_name и cuisine_type. Создайте метод describe_restaurant(),
который выводит два атрибута, и метод open_restaurant(),
который выводит сообщение о том, что ресторан открыт.

Создайте на основе своего класса экземпляр с именем restaurant.
Выведите два атрибута по отдельности, затем вызовите оба метода.

'''

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''' метод выводит название ресторана и кухню'''
        name_type = f"\nРесторан:{self.restaurant_name}, Кухня:{self.cuisine_type}."
        return name_type.title()

    # def describe_restaurant_name(self):
    #     '''' метод выводит название ресторана'''
    #     name_rest = f"Название ресторана: {self.restaurant_name}"
    #     return name_rest.title()

    # def describe_restaurant_cuisine(self):
    #     '''' метод выводит  кухню ресторана'''
    #     cuisine_rest = f"Кухня в ресторане: {self.cuisine_type}"
    #     return cuisine_rest.title()

    def open_restaurant(self):
        '''' метод выводит  информацию, что ресторан открыт'''
        return "Ресторан открыт"






restaurant = Restaurant('Уральские пельмени', 'пельмени и варенники' )

print(f'Ресторан называется: {restaurant.restaurant_name}.') # название ресторана
print(f'Кухня ресторана: {restaurant.cuisine_type}.') # кухня ресторана
print('Название ресторана и кухня: ',restaurant.describe_restaurant()) # # печатаю название и тип кухни в ресторане
print(restaurant.open_restaurant()) # сообщение, что ресторан открыт

print(restaurant.describe_restaurant(), restaurant.open_restaurant()) # Имя и кухня ресторана + сообщение, что ресторан открыт





print()
print('    -2. Начните с класса из упражнения 1.')
'''
2. Начните с класса из упражнения 1. 
Создайте три разных экземпляра, вызовите для каждого экземпляра метод describe_restaurant().

'''
restaurant_1 = Restaurant('кафе Пушкин', ' Старинная, русская с элементами фрагцузской')
print(restaurant_1.describe_restaurant())

restaurant_2 = Restaurant('Руккола', 'Итальянская')
print(restaurant_2.describe_restaurant())

restaurant_3 = Restaurant('Тануки', 'Японская')
print(restaurant_3.describe_restaurant())



print()
print('    -3. Создайте класс с именем User. ')

'''
3. Создайте класс с именем User. 
Создайте два атрибута first_name и last_name, 
а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя. 
Напишите метод describe_user(), который выводит сводку с информацией 
о пользователе. 

Создайте еще один метод greet_user() 
для вывода персонального приветствия для пользователя.
Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба метода для каждого пользователя.

'''
class User():
    def __init__(self, first_name, last_name, age, gender ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        info_user = f"\nИмя: {self.first_name}\nФамилия: {self.last_name}\nВозраст: {self.age}\nПол: {self.gender}."
        return info_user.title()

    def greet_user(self):
        hi = f" Привет {self.first_name} {self.last_name} !!!"
        return hi.title()

us_1 = User('Анна', 'Иванова', '30', 'female')
print(us_1.describe_user())
print(us_1.greet_user())

us_2 = User('Елена', 'Булкина', '28', 'female')
print(us_2.describe_user(),   us_2.greet_user()) # не работает у меня здесь \n и \r, не знаю почему

us_3 = User('Семен', 'Семенов', '35', 'male')
print(us_3.describe_user(),   us_3.greet_user()) # не работает у меня здесь \n и \r, не знаю почему



print()
print('    -4. Начните с программы из упражнения 1. ')
'''
4. Начните с программы из упражнения 1. 
Добавьте атрибут number_served со значением по умолчанию 0; 
он представляет количество обслуженных посетителей. 
Создайте экземпляр с именем restaurant. 
Выведите значение number_served, потом измените и выведите снова.


Добавьте метод с именем set_number_served(), позволяющий задать количество обслуженных посетителей. 
Вызовите метод с новым числом, снова выведите значение.

Добавьте метод с именем increment_number_served(), 
который увеличивает количество обслуженных посетителей на заданную величину. 
Вызовите этот метод с любым числом, которое могло бы представлять 
количество обслуженных клиентов, — скажем, за один день.

'''
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name # имя ресторана
        self.cuisine_type = cuisine_type # тип кухни
        self.number_served = 0 # количество обслуженных посетителей

    def describe_restaurant(self):
        '''' метод выводит название ресторана и кухню'''
        name_type = f"\nРесторан:{self.restaurant_name}, Кухня:{self.cuisine_type}."
        return name_type.title()


    def open_restaurant(self):
        '''' метод выводит  информацию, что ресторан открыт'''
        return "Ресторан открыт"

restaurant_ns = Restaurant('Циплята табака', 'Блюда из ципленка')
print('Количество обслуженных столиков: ', restaurant_ns.number_served)

print('\n Способ 1.\nПрямое изменение атрибута number_served (количество обслуженных посетителей). Так Не рекомендуется!!!')
restaurant_ns.number_served = 30 # меняем значение на 30
print('Количество обслуженных столиков: ', restaurant_ns.number_served) # контрольная распечатка

print('\n Способ 2.\nИзменение значения атрибута с использованием метода')
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name # имя ресторана
        self.cuisine_type = cuisine_type # тип кухни
        self.number_served = 0 # количество обслуженных посетителей

    def describe_restaurant(self):
        '''' метод выводит название ресторана и кухню'''
        name_type = f"\nРесторан:{self.restaurant_name}, Кухня:{self.cuisine_type}."
        return name_type.title()


    def open_restaurant(self):
        '''' метод выводит  информацию, что ресторан открыт'''
        return "Ресторан открыт"

    def set_number_served(self, s_num_ser):
        ''' метод для изменения атрибута: number_served (количество обслуженных посетителей)'''
        self.number_served = s_num_ser


restaurant_ns = Restaurant('Циплята табака', 'Блюда из ципленка')
print('Количество обслуженных столиков до изменения: ', restaurant_ns.number_served)

restaurant_ns.set_number_served(120) # меняю количество облуженных столиков на 120

print('Количество обслуженных столиков после изменения методом set_number_served : ', restaurant_ns.number_served)



print('\n Способ 3.\nИзменение значения атрибута с приращением')

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name # имя ресторана
        self.cuisine_type = cuisine_type # тип кухни
        self.number_served = 0 # количество обслуженных посетителей

    def describe_restaurant(self):
        '''' метод выводит название ресторана и кухню'''
        name_type = f"\nРесторан:{self.restaurant_name}, Кухня:{self.cuisine_type}."
        return name_type.title()


    def open_restaurant(self):
        '''' метод выводит  информацию, что ресторан открыт'''
        return "Ресторан открыт"

    def set_number_served(self, s_num_ser):
        ''' метод для изменения атрибута: number_served (количество обслуженных посетителей'''
        self.number_served = s_num_ser

    def increment_number_served(self, qty):
        ''' метод меняет атрибут number_served (количество обслуженных посетителей, приращением (зависит от знака)'''
        self.number_served += qty
restaurant_ns = Restaurant('Циплята табака', 'Блюда из ципленка')
print('Количество обслуженных столиков до изменения: ', restaurant_ns.number_served)

restaurant_ns.increment_number_served(50) # меняю количество облуженных столиков на 120

print('Количество обслуженных столиков после изменения методом set_number_served : ', restaurant_ns.number_served)



print()
print('    -5. Попытки входа: добавьте атрибут login_attempts в класс User из упражнения ')

'''
5. Попытки входа: добавьте атрибут login_attempts в класс User из упражнения 3. 
Напишите метод increment_login_attempts(), увеличивающий значение login_attempts на 1. 
Напишите другой метод с именем reset_login_attempts(), обнуляющий значение login_attempts.

Создайте экземпляр класса User и вызовите increment_login_attempts() несколько раз. 
Выведите значение login_attempts, чтобы убедиться в том, что значение было изменено правильно, 
а затем вызовите reset_login_attempts(). 
Снова выведите login_attempts и убедитесь в том, что значение обнулилось.

'''
class User():
    def __init__(self, first_name, last_name, age, gender ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        info_user = f"\nИмя: {self.first_name}\nФамилия: {self.last_name}\nВозраст: {self.age}\nПол: {self.gender}."
        return info_user.title()

    def greet_user(self):
        hi = f" Привет {self.first_name} {self.last_name} !!!"
        return hi.title()

    def increment_login_attempts(self, qty):
        ''' метод должен увеличивать значение login_attempts на 1 не зависимо от значение qty '''
        self.login_attempts = self.login_attempts +1

    def reset_login_attempts(self):
        self.login_attempts = 0


new_user = User('Светлана', 'Чижикова', '27', 'жен.') # создал новый экземпляр new_user класса User

print('Значение login_attempts до изменения: ',new_user.login_attempts)
new_user.increment_login_attempts(20) # меняю значение login_attempts.
print('Значение login_attempts ПОСЛЕ изменения 1 : ',new_user.login_attempts)

new_user.increment_login_attempts(0) # повторно №2 меняю значение login_attempts.
new_user.increment_login_attempts(-100000) # повторно №3 меняю значение login_attempts.

print('Значение login_attempts после трех изменений : ',new_user.login_attempts)


new_user.reset_login_attempts() # сбрасываю значение login_attempts на ноль
print('Значение login_attempts после сбрасывания: ', new_user.login_attempts)


print()
print('    -6. Киоск с мороженым')

'''
6. Киоск с мороженым — особая разновидность ресторана. Напишите класс IceCreamStand, 
наследующий от класса Restaurant из упражнения 1 или упражнения 4. 
Подойдет любая версия класса; просто выберите ту, которая вам больше нравится. 

Добавьте атрибут с именем flavors для хранения списка сортов мороженого. 
Напишите метод, который выводит этот список. 
Создайте экземпляр IceCreamStand и вызовите этот метод.


'''

class Restaurant(): # ДЛя создания нового класса 'IceCreamStand' наследника от 'Restaurant' напишу class Restaurant()
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name # имя ресторана
        self.cuisine_type = cuisine_type # тип кухни
        self.number_served = 0 # количество обслуженных посетителей

    def describe_restaurant(self):
        '''' метод выводит название ресторана и кухню'''
        name_type = f"Ресторан:{self.restaurant_name}, Кухня:{self.cuisine_type}."
        return name_type.title()


    def open_restaurant(self):
        '''' метод выводит  информацию, что ресторан открыт'''
        return "Ресторан открыт"

    def set_number_served(self, s_num_ser):
        ''' метод для изменения атрибута: number_served (количество обслуженных посетителей'''
        self.number_served = s_num_ser

    def increment_number_served(self, qty):
        ''' метод меняет атрибут number_served (количество обслуженных посетителей, приращением (зависит от знака)'''
        self.number_served += qty

class IceCreamStand(Restaurant): # Это класс потомок от класса Restaurant
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 'Ваниль', 'Шоколад', 'Клубника', 'Томат'

    def show_flavors(self):
        show = f'вкусы мороженого: {self.flavors}'
        return show.title()


my_ice_cream = IceCreamStand('Павильон мороженое', 'Сорбеты и мороженое') # создал экземпляр на основе класса потомка

print(my_ice_cream.describe_restaurant()) # распечатываю экземпляр my_ice_cream класса потомка IceCreamStand

print(f'Вкусы: {my_ice_cream.flavors}') # распечатал вкусы прямым способом
print("Вывожу вкусы мороженого через метод 'show_flavors': ",  my_ice_cream.show_flavors()) # распечатал вкусы при помощи метода






print()
print('    -7. Администратор — особая разновидность пользователя. ')

'''
7. Администратор — особая разновидность пользователя. 
Напишите класс с именем Admin, наследующий от класса User из упражнения 3 или упражнения 5. 

Добавьте атрибут privileges для хранения списка строк вида "разрешено добавлять сообщения", 
"разрешено удалять пользователей", "разрешено банить пользователей" и т. д. 

Напишите метод show_privileges() для вывода набора привилегий администратора. 

Создайте экземпляр Admin и вызовите свой метод.

'''

class User(): # это класс будет супер классом
    def __init__(self, first_name, last_name, age, gender ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        info_user = f"\nИмя: {self.first_name}\nФамилия: {self.last_name}\nВозраст: {self.age}\nПол: {self.gender}."
        return info_user.title()

    def greet_user(self):
        hi = f" Привет {self.first_name} {self.last_name} !!!"
        return hi.title()

    def increment_login_attempts(self, qty):
        ''' метод должен увеличивать значение login_attempts на 1 не зависимо от значение qty '''
        self.login_attempts = self.login_attempts +1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User): # Это класс потомок
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = "разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей", "разрешено модерировать чат"


    def show_privileges(self):
        show_priv = f"Администратору разрешено:\n {self.privileges}  и не только... "
        return show_priv.title()

admin = Admin('Арина', 'Синичкина', '98', 'n/d') # создал новый экземпляр
print('Проверка пользователя admin: ', admin.describe_user()) # конторльная распечатка данных

#print(admin.self.privileges()) # не получается распечатать на прямую почему то???
print(admin.show_privileges()) # не знаю, как убрать скобки при выводе


print()
print('    -8. Напишите класс Privileges.')
'''
8. Напишите класс Privileges. 
Класс должен содержать всего один атрибут privileges со списком строк из упражнения 7. 

Переместите метод show_privileges() в этот класс. 

Создайте экземпляр Privileges как атрибут класса Admin. 

Создайте новый экземпляр Admin и используйте свой метод для вывода списка привилегий.


'''

class Privileges():
    def __init__(self, privileges):
        self.privileges = "разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей", "разрешено модерировать чат"

    def show_privileges(self): # выводит список, что разрешено админу
        print(f"Администратору разрешено: {self.privileges}. ")

poi = Privileges("разрешено добавлять сообщения") # создал экземпляр
poi.show_privileges() # проверка метода по выводу прав админа


''' 
План: 
ДЛя того, что бы создать экземпляр Privileges как атрибут класса Admin
-Я сначала пишу родительский класс (Super Class) User,
 
-дальше создаю класс потомок  Admin , класс Privileges

-который помещу в параметры класса Admin )))

'''

class User(): # это класс будет супер классом для потомка админ
    def __init__(self, first_name, last_name, age, gender ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        info_user = f"\nИмя: {self.first_name}\nФамилия: {self.last_name}\nВозраст: {self.age}\nПол: {self.gender}."
        return info_user.title()

    def greet_user(self):
        hi = f" Привет {self.first_name} {self.last_name} !!!"
        return hi.title()

    def increment_login_attempts(self, qty):
        ''' метод должен увеличивать значение login_attempts на 1 не зависимо от значение qty '''
        self.login_attempts = self.login_attempts +1

    def reset_login_attempts(self):
        self.login_attempts = 0





class Privileges():
    def __init__(self, privileges=" 'разрешено добавлять сообщения',  'разрешено удалять пользователе', 'разрешено банить пользователей', 'разрешено модерировать чат' " ):
        self.privileges = privileges # меня смущает мое оформление, именно эта длинная строка в self __init__. Может это можно как то короче оформить?

    def show_privileges(self): # выводит список, что разрешено админу
        print(f"Администратору разрешено: {self.privileges}. ")





class Admin(User): # Это класс потомок в него в параметры я размещу класс Privileges()
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()  # здесь я создаю параметр из экземпляра


    def show_privileges(self):
        show_priv = f"Администратору разрешено:\n {self.privileges}  и не только... "
        return show_priv.title()


new_2 = Admin('Дядя', 'Степа', '150', 'муж.') # создали экземпляр
print(new_2.describe_user()) # контрольная описательная распечатка
new_2.privileges.show_privileges()



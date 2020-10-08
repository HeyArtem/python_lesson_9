

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
        self.login_attempts = +1

    def reset_login_attempts(self):
        self.login_attempts = 0


new_user = User('Светлана', 'Чижикова', '27', 'жен.') # создал новый экземпляр new_user класса User

print('Значение login_attempts до изменения: ',new_user.login_attempts)
new_user.increment_login_attempts(20) # меняю значение login_attempts.
print('Значение login_attempts ПОСЛЕ изменения: ',new_user.login_attempts)
new_user.reset_login_attempts() # сбрасываю значение login_attempts на ноль
print('Значение login_attempts после сбрасывания: ', new_user.login_attempts)











# 1 Не пойму как работает
"""
Наследование
Наследование подразумевает то, что дочерний класс содержит все атрибуты
родительского класса, при этом некоторые из них могут быть переопределены
или добавлены в дочернем.
Например, мы можем создать свой класс, похожий на словарь:

"""

class My_dict(dict):
    def get(self, key, default = 0):
        return dict.get(self, key, default)

a = dict(a=1, b=2)
b = My_dict(a = 1, b= 2)

b['c'] = 4  # что это??, я не помню
print(b)

print(a.get('v')) # что это??, не пойму

print(b.get('v')) # что это??,

"""
Класс Mydict ведёт себя точно так же, как и словарь, 
за исключением того, что метод get по умолчанию возвращает не None, а 0.

"""

# 2

print('     Вопрос 2')
import random

class Dice:
    def __init__(self, N):
        self.throw_num = N # Броски
        self.current_throw = 0 # Параметр отвечает за количество совершенных бросков

    def set_hidden_numbers(self):  # настройка параметров бросания костей
        self._hidden_num_1 = random.randint(1,6)  # _'земля' в начале, значит, что параметры скрытые
        self._hidden_num_2 = random.randint(1,6)


    def throw_dices(self):
        dice_1 = random.randint(1, 6) # бросаем кости
        dice_2 = random.randint(1, 6) # бросаем кости 2
        self.current_throw+=1

        if self.current_throw > self.throw_num:              # если количество бросков превысило запланированное
            raise Exception("Вы превысили количество попыток! ")

        if {dice_1,dice_2} == {self._hidden_num_1, self._hidden_num_2}: # Почему оформлено, как множество (только уникальные элементы?)
            return True
        else:
            return False

if __name__ == "__main__": # Что это???
    dice_game = Dice(1)
    dice_game.set_hidden_numbers()
    print(dice_game._hidden_num_1, dice_game._hidden_num_2) # почему обращаемся через dice_game?
    print()
    for i in range(1):  # зачем Dice=20 и range=100?
        try:
            print(dice_game.throw_dices())
        except:
            print("Игра закончена")

# 30/08/2020
""""
1. __name__ - эта переменная равна строке __main__,
  когда скрипт запускается напрямую,
  и равна имени модуля, когда импортируется
  Переменная __name__ чаще всего используется, чтобы указать, что определенная часть кода
должна выполняться, только когда модуль выполняется напрямую:
  
2. __file__ - эта переменная равна имени скрипта,
  который был запущен напрямую,
  и равна полному пути к модулю, когда он импортируется

"""

# 3.
print("    пример  __name__ : ")


def multiply(a, b):
    return a * b

if __name__ == "__main__":  # что здесь происходит, для чего такие обряды?
    print(multiply(3, 5))

wtf = multiply(6, 6)  # так работает же,,,
print(wtf)

# 4.
print('  4.')
class IPAddress:
    def __init__(self, ip):
        self.ip = ip


ip1 = IPAddress('10.1.1.1')
print(ip1)
''''
Будет вывод:
<__main__.IPAddress object at 0x0359CD48>

Вопрос: Это номер ячейки, где хранится информация?
 
'''
# 5.
print('  5.')
print(' с применением __repr__ через класс: ')

class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return f" через (str)-->IPAddress: {self.ip} "

    def __repr__(self):
        return f" через (repr)-->IPAddress: ('{self.ip}')"

ip1 = IPAddress('10.1.1.1')
ip2 = IPAddress('10.2.2.2')

ip_addresses = [ip1, ip2]

print(ip_addresses)

print('печать ПЕРВОГО через класс: ',repr(ip1))
''''
Вопрос: почему автоматически используется только метод __repr__,
        а метод __str__ не используется?

'''
# 6.
print('  6.')
''''
В Python 3 была удалена встроенная функция cmp вместе со специальным методом __cmp__ .

Из документации: Функция cmp() следует рассматривать как ушедшую, 
а специальный метод __cmp__() больше не поддерживается. 
Используйте __lt__() для сортировки __eq__() с __hash__() и другими богатыми сравнениями 
по мере необходимости. (Если вам действительно нужна функция cmp() , 
вы можете использовать выражение (a > b) - (a < b) как эквивалент для cmp(a, b) .)

А в примере с картами она используется...?
'''

class A(object):
  def __init__(self, name, age, other):
    self.name = name
    self.age = age
    self.other = other
  def __cmp__(self, other):
    assert isinstance(other, A) # assumption for this example
    return cmp((self.name, self.age, self.other),
               (other.name, other.age, other.other))
asd = A('Lora', 39, 'women')
#print(asd.__cmp__('women')) # будет ошибка
print(asd)
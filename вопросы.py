
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
    dice_game = Dice(20)
    dice_game.set_hidden_numbers()
    print(dice_game._hidden_num_1, dice_game._hidden_num_2) # почему обращаемся через dice_game?
    for i in range(100):  # зачем Dice=20 и range=100?
        try:
            print(dice_game.throw_dices())
        except:
            print("Игра закончена")
# 9.4. Принципы ООП. Полиморфизм, Инкапсуляция, Наследование
# difficult = трудный

from dice_game import Dice
import random


#d = Dice(10) # просто проверка что прога импортирована и работает


class Dice_dif(Dice):
    """
    Допишем режимы игры в кости

    type 1: совпали, как неупорядоченная пара
    type 2: совпало, хотя бы одно значение
    type 3: совпала сумма

    """
    def __init__(self, N, type):  # сразу вписал type?
        super().__init__(N)         # вызвали родительский init
        self.type_game = type       # и немного его дописали(init)


    def throw_dices(self):                          # скопировали из class Dice
        dice_1 = random.randint(1, 6) # бросаем кости
        dice_2 = random.randint(1, 6) # бросаем кости 2
        self.current_throw+=1


        if self.current_throw > self.throw_num:  # если количество бросков превысило запланированное
            raise Exception("Вы превысили количество попыток! ")

        if self.type_game == 1:
            if {dice_1,dice_2} == {self._hidden_num_1, self._hidden_num_2}: # Почему оформлено, как множество (только уникальные элементы?)
                return True
            else:
                return False

        elif self.type_game == 2:
            if (dice_1 in {self._hidden_num_1, self._hidden_num_2}) or (dice_2 in {self._hidden_num_1, self._hidden_num_2}):
                print("Attemp type 2: ", dice_1, dice_2) # будем видеть сколько было изначально и сколько выпало на костях
                return True
            else:
                return False

        elif self.type_game == 3:  # если сумма совпадает
            if dice_1 + dice_2 == self._hidden_num_1 + self._hidden_num_2:
                print("Attemp type 3: ", dice_1, dice_2)
                return True
            else:
                return False


if __name__ == "__main__":
    dice_game = Dice_dif(3, 3) # количество бросков и тип игры
    dice_game.set_hidden_numbers()
    print(dice_game._hidden_num_1, dice_game._hidden_num_2)  # почему обращаемся через dice_game?
    for i in range(4):  # зачем Dice=..  и range=..?
        try:
            print(dice_game.throw_dices())
        except:
            print("Игра закончена")








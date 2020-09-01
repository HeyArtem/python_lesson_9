# ДЗ после 9 главы

# Реализовать класс для карточный игры "Игра в дурака" в простейшем виде
# (без козырей, можно без добора карт и т.д.).
#
# Структурв класса может быть на ваше устмотрение. Можно реализовать следующие методы:
# инициализация игры(раздача карт себе и компьютеру) ход ваш, ход компьтера.
#
# PRO Реализовать класс для карточной игры "Игра в дурака" как можно ближе к правилам
# (можно реализовать на ваш выбор, в котором будет представлен пройденый на уроке функционал

from __future__ import print_function, division
import random


class Card(object):
    """"
    Представляет стандартную игральную карту.
         Атрибуты :
         suit (масть): integer 0-3
         rank (ранг): integer 1-9

    """


    def __init__(self, suit, rank=2):
        self.suit = suit  # атрибут экз-ра класса
        self.rank = rank  # атрибут экз-ра класса

    suit_names = ['Clubs', 'Dianonds', 'Hearts', 'Spades']
    rank_names = [None, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']


    def __str__(self):   # является объектом типа Card
        """" Возвращает удобочитаемое представление  """
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])


# # пробую распечатать карты
# card_1 = Card(0, 1)
# print('выводим rank & suit:' , card_1)


    def __eq__(self, other):
        ''''
        ПРоверка, совпадает ли ранг и масть у себя и других
        Возвращает логическое (boolean)
        '''
        return self.suit == other.suit and self.rank == other.rank

    def __it__(self, other):
        ''''
        Сравнивает карты с другими, сначало по масти, затем по рангу
        Compares this card to other, first by suit, then rank
        :returns boolean

        '''
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2   # вот здесь... где то было не так

class Deck:
    ''''
        Represents a deck of cards.
        Attributes:
            cards: list of Card objects.

        Представляет собой колоду карт.
        Атрибуты: список карт

    '''

    def __init__(self):
        ''''
        Initializes the Deck with 52 cards.
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1, 10):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        ''''
         Returns a string representation of the deck
         Возвращает строковое представление колоды
        '''
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def __add__(self, card):
        ''''
        Adds a card to the deck.
        card: Card
        '''
        self.cards.append(card)

    def remove_card(self, card):
        ''''
        Removes a card from the deck or raises exception if it is not there.
        card: Card

        Удаляет карту из колоды или вызывает исключение, если ее нет
        '''
        self.cards.remove(card)

    def pop_card(self, i=-1):
        ''''
        Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card.

        Снимает и возвращает карту из колоды.
         i: индекс карточки, которую нужно открыть; по умолчанию выскакивает последняя карточка.

        '''
        return self.cards.pop(i)

    def shuffles(self):
        '''' Shuffles the cards in this deck    '''
        random.shuffle(self, cards)

    def sort(self):
        ''''
        Sorts the cards in ascending order.

        Сортировка карточек по возрастанию.
        '''

    def move_cards(self, hand, num):
        ''''
        Moves the given number of cards from the deck into the Hand.
        hand: destination Hand object
        num: integer number of cards to move

        Перемещает заданное количество карт из колоды в руку.
         рука: пункт назначения Hand объект
         num: целое число карт для перемещения

        '''
        for i in range(num):
            hand.add_card(self.pop_card())



class Hand(Deck):
    ''''
    Represents a hand of playing cards.
    '''
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def find_defining_class(obj, method_name):
        ''''
        Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.

     obj: any python object
    method_name: string method name



    Находит и возвращает объект класса, который предоставит
     определение method_name (в виде строки), если это
     вызывается на obj.

          obj: любой объект Python
     method_name: строковое имя метода


        '''

        for ty in type(obj).mro():  # что это?
            if method_name in ty.__dict__:
                return ty
        return None

    if __name__ == '__main__':
        deck = Deck()
        deck.shuffles()

        hand = Hand()
        print(find_defining_class(hand, 'shuffle'))

        deck.move_cards(hand, 5)
        hand.sort()
        print(hand)















#
#     def __cmp__(self, other):
#         """" Сравнение мастей """
#         if self.suit > other.suit: return 1
#         if self.suit < other.suit: return -1
#
#         """" Если масти совпадают --> сравнение Рангов """
#         if self.rank > other.rank: return 1
#         if self.rank < other.rank: return -1
#
#         """" Ранги совпадают  --> Ничья"""
#         return 0
#
#
# Ниже другой способ такого же сравнения
#


#     def __cmp__(self, other):
#         t1 = self.suit, self.rank
#         t2 = other.suit, other.rank
#         return cmp (t1, t2) # или return t1 < t2, как в коде def __eq__
#
#
#
# class Deck(object):
#     """" Это колода карт """
#
#     def __init__(self):
#
#         self.cards = []
#         for suit in range(4):
#             for rank in range(1, 10):
#                 card = Card(suit, rank)
#                 self.cards.append(card)
#
#     def __str__(self):
#         """" Возвращает строковое представление колоды. """
#         res = []
#         print('res: ', res)
#         for card in self.cards:
#             res.append(str(card))
#         return '\n'.join(res)
#
# deck = Deck()
# print(deck)
#
#     def pop_card(self):
#         return self.cards.pop()
#













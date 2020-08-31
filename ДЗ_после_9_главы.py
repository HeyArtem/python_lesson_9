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













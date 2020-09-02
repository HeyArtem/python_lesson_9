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


class Card:
    def __init__(self, suit=0, rank=2):
        self.suit = suit  # атрибут экз-ра класса
        self.rank = rank  # атрибут экз-ра класса

    suit_names = ['Clubs', 'Dianonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']


    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])


# # пробую распечатать карты
# card_1 = Card(0, 1)
# print('выводим rank & suit:' , card_1)


    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):

        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2   # вот здесь... где то было не так

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def pop_card(self, i=-1):
        return self.cards.pop(i)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())



class Hand(Deck):
    def __init__(self,label=''):
        self.cards = []
        self.label = label

    def find_defining_class(obj, method_name):
        for ty in type(obj).mro():        # что это?
            if method_name in ty.__dict__:
                return ty
        return None

    if __name__ == '__main__':  # опять это?
        deck = Deck()
        deck.shuffle()

        hand = Hand()
        print(find_defining_class(hand, 'shuffle'))

        deck.move_cards(hand, 5)
        hand.sort()
        print(hand)























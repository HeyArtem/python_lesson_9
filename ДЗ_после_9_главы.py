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
    ''''
    Represents a standard playing card.

    Attributes:
      suit: integer 0-3
      rank: integer 1-10

    '''
    suit_names = ['Крести ♧', 'Буби ♢', 'Черви ♡', 'Пики ♠']
    rank_names = [None, '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']



    def __init__(self, suit=0, rank=2):
        self.suit = suit  # атрибут экз-ра класса
        self.rank = rank  # атрибут экз-ра класса




    def __str__(self):
        ''''
        Returns a human-readable string representation.

        Возвращает удобочитаемое строковое представление.
        '''

        return '%s масть %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])


    def __eq__(self, other):
        ''''
        Checks whether self and other have the same rank and suit.
        returns: boolean

        Проверяет, совпадают ли ранг и масть у себя и других.
         возвращает: логическое

        '''
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        ''''
        Compares this card to other, first by suit, then rank.
        returns: boolean

        Сравнивает эту карту с другими, сначала по масти, затем по рангу.
         возвращает: логическое

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
     Атрибуты:
       карты: список объектов Карты.
    '''

    def __init__(self):
        ''''
        Initializes the Deck with 36 cards.

        '''

        self.cards = []
        for suit in range(4):
            for rank in range(1, 10):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        ''''
        Returns a string representation of the deck.

        Возвращает строковое представление колоды.

        '''
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        ''''
        Adds a card to the deck.
        card: Card

        Добавляет карту в колоду.
         card: Карта

        '''
        self.cards.append(card)

    def remove_card(self, card):
        ''''
        Removes a card from the deck or raises exception if it is not there.

        Удаляет карту из колоды или вызывает исключение, если ее нет.

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

    def shuffle(self):
        ''''
        Shuffles the cards in this deck.

        Перетасовывает карты в этой колоде.

        '''

        random.shuffle(self.cards)

    def sort(self):
        ''''
        Sorts the cards in ascending order

        Сортировка карточек в порядке возрастания

        '''

        self.cards.sort()

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

    Представляет собой руку игральных карт.

    '''

    def __init__(self,label=''):
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

    for ty in type(obj).mro():        # что это?
        if method_name in ty.__dict__:
            return ty
    return None

if __name__ == '__main__':  # опять это?
    deck = Deck()
    deck.shuffle()

    hand = Hand()
    print(find_defining_class(hand, 'shuffle'))

    deck.move_cards(hand, 6)
    hand.sort()
    print(hand)























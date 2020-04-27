import cards
from cards import Card
import random

class Deck:

    def __init__(self):
        self.deck = []
        for suit in cards.suits:
            for rank in cards.ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' +card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
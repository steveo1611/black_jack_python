# Milestone Project-2 : Blackjack Game
'''
requirements:
You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...

And most importantly:

You must use OOP and classes in some portion of your game. You can not just use functions in your game. 
Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!
'''

from cards import Card
from deck import Deck
from hand import Hand
playing = True

test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
test_player.value

for card in test_player.hand_cards:
    print(card)

print(test_player.value)
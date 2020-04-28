# Milestone Project-2 : Blackjack Game
from cards import Card
from deck import Deck
from hand import Hand
from chips import Chips

card = Card
deck = Deck
hand = Hand
chip = Chips

playing = True

def take_bet(chip):
    while True:
        try:
            chip.bet = int(input('Please enter your bet now: '))
        except ValueError:
            print('Sorry, a bet must be a whole number!')
        else:
            if chip.bet > chip.total:
                print("Sorry, your bet can't exceed",chip.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing
    
    while True:
        move = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        if move[0].lower() == 'h':
            hit(deck,hand)
        elif move[0].lower() == 's':
            playing = False
        else:
            print('Sorry, please try again.')
            continue
        break

def show_ingame_cards(player, dealer):
        print("\nDealer's Hand:")
        print(" <card hidden> ")
        print('', dealer.hand_cards[1])
        print("\nPlayer's Hand:", *player.hand_cards, sep =' \n')
        print("current total:",player.value)


'''
    for card in player.hand_cards:
        print('Players cards:')
        print(card)
    for dcard in dealer.hand_cards:
        print('Dealer is showing:')
        print(dcard[0])
'''


def show_endgame_cards(player,dealer):
    print("\nDealer's Hand:", *dealer.hand_cards, sep='\n')
    print("Dealer's Hand = ", dealer.value)
    print("\nPlayer's hand", *player.hand_cards, sep='\n')
    print("Player's Hand =", player.value)


def player_bust(player,dealer,chips):
    print("Player busts!")
    chip.lose_bet(chips)

def player_win(player,dealer,chips):
    print("Player Wins!!!!")
    chip.win_bet(chips)

def dealer_bust(player,dealer,chips):
    print("Dealer Busts!!!")
    chip.win_bet(chips)
    
def dealer_wins(player,dealer,chips):
    print("Dealer Wins!!!")
    chip.lose_bet(chips)

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    print("Welcome to M-2 Black Jack game")
    game_deck = deck()
    game_deck.shuffle()
    chip_tot = chip()
    while True:
        player_hand = hand()
        dealer_hand = hand()
        player_hand.add_card(game_deck.deal())
        dealer_hand.add_card(game_deck.deal())
        player_hand.add_card(game_deck.deal())
        dealer_hand.add_card(game_deck.deal())
        take_bet(chip_tot)
        show_ingame_cards(player_hand, dealer_hand)
        while playing:
            hit_or_stand(game_deck,player_hand)
            show_ingame_cards(player_hand, dealer_hand)
            if player_hand.value > 21:
                player_bust(player_hand, dealer_hand, chip_tot)
                break
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(game_deck,dealer_hand)
                show_endgame_cards(player_hand,dealer_hand)
            if dealer_hand.value > 21:
                dealer_bust(player_hand, dealer_hand, chip_tot)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,chip_tot)
            elif dealer_hand.value < player_hand.value:
                player_win(player_hand,dealer_hand,chip_tot)
            else:
                push(player_hand, dealer_hand)

        print("\nPlayer's winnings stand at", chip_tot.total)

        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break
    break

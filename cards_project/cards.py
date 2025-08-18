import random

"""
object deck of cards
object card
    attrs:
        suit
        rank
    methods:
        beats other card

object player
object player's hand

object stock

object desk

object discard

dict rank
"""


NUM_CARDS = 36
ranks = {'6': 1, '7': 2, '8': 3, '9': 4, '10': 5, 'J': 6, 'Q': 7, 'K': 8, 'A': 9}
suits = ("spades", "hearts", "diamonds", "clubs")

class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show_card(self):
        print("Rank: ", self.rank, ", suit: ", self.suit)

class deck_36:

    def __init__(self):
        self.cards = []

        for rank in list(ranks.keys()):
            for suit in suits:
                new_card = card(rank, suit)
                self.cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, card_no):
        return self.cards.pop(card_no)

deck = deck_36()

for i in range(NUM_CARDS):
    curr_card = deck.cards[i]
    curr_card.show_card()

print("Shuffling cards")

deck.shuffle()

for i in range(NUM_CARDS):
    curr_card = deck.cards[i]
    curr_card.show_card()
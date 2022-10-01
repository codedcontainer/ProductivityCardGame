"""Deck of playing cards and actions"""
import random
from Model.Card import Card


class CardDeck:
    """Standard deck of cards (52 cards); draw pile"""
    suits = ['h', 'd', 'c', 's']
    values = list(range(1, 14))
    cards = []

    def __init__(self):
        self.reset()

    def create(self):
        "Creates list of cards from list of values and suits"
        for value in self.values:
            for suit in self.suits:
                card = Card(value, suit)
                self.cards.append(card)

    def add_joker(self, amount):
        "Creates and adds x number of jokers to the deck"
        joker_list = [Card(0, "j") for joker in range(1, amount + 1)]
        self.cards = self.cards + joker_list

    def discard_joker(self):
        """Removes joker card from deck"""
        if len(self.cards) > 0:
            self.cards.pop(0)

    def shuffle(self):
        "Shuffles cards in deck"
        cards = self.cards
        card_count = len(cards)
        if card_count > 0:
            for card in enumerate(cards):
                index = card[0]
                value = card[1]
                random_int = random.randint(1, card_count - 1)
                random_card = cards[random_int]
                cards[index] = random_card
                cards[random_int] = value

    def append_pile(self, pile):
        """Appends a pile to the deck and removes all cards from that pile"""
        if len(pile.cards) > 0:
            self.cards += pile.cards
            pile.empty()

    @property
    def draw(self):
        "Removes and returns the top card of the deck"
        card = self.cards[0]
        self.cards.pop(0)
        return card

    def reset(self):
        """Remove all cards and re-creates a new deck"""
        self.cards = []
        self.create()
        self.add_joker(2)
        self.shuffle()

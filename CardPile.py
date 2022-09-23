"Describes a pile of playing cards"
from Timing import Timing
from Card import Card

class CardPile:
    "Card pile"
    def __init__(self, name):
        self.name = name
        self.cards = []

    def empty(self):
        "remove all cards from the pile"
        self.cards = []

    def add(self, card):
        "add a card to the pile"
        self.cards.append(card)

    def sum_card_values(self):
        "return the sum value of all cards"
        sum_card_values = 0
        for card in self.cards:
            sum_card_values = sum_card_values + card.value
        return sum_card_values

    def sort_ascending(self):
        "sorts all cards by value starting with smallest value"
        return sorted(self.cards, key=lambda cards: cards.value)

    def sort_descending(self):
        "sorts all cards by value starting with largest value"
        return sorted(self.cards, key=lambda cards: cards.value, reverse = True)

    def add_to_discard(self, discard):
        "add cards to the discard pile"
        if self.cards is not None:
            discard.cards = discard.cards + self.cards
            self.cards = []

    def remove_many_minutes(self, minutes):
        "remove cards by target in minutes"
        cards = self.sort_descending()
        for card in cards:
            if minutes - card.value > 0 :
                cards.pop(0)

    def print_cards(self):
        "print all of the cards as a string"
        cards = [Card.AsString(card) for card in self.cards]
        return ",".join(cards)

    def print_sum_value(self):
        "print the sum card valus as a string"
        _sum_card_values = self.sum_card_values()
        self.print_cards()
        timing = Timing()
        timing.print_time(_sum_card_values, self.name)

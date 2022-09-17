from Timing import Timing
from Card import Card

class CardPile:
    "Describes a pile of playing cards"
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def empty(self):
        self.card = []
    
    def add(self, card):
        self.cards.append(card)

    def sum_card_values(self):
        sum = 0
        for card in self.cards:
            sum = sum + card.value
        return sum

    def sort_ascending(self):
        return sorted(self.cards, key=lambda cards: cards.value)

    def sort_descending(self):
        return sorted(self.cards, key=lambda cards: cards.value, reverse = True)

    def add_to_discard(self, discard):
        if(self.cards is not None):
            discard.cards = discard.cards + self.cards
            self.cards = []

    def remove_many_minutes(self, minutes):
        cards = self.sort_descending()
        for card in cards:
            if(minutes - card.value > 0):
                cards.pop(0)        

    def print_cards(self):
        cards = [Card.AsString(card) for card in self.cards]
        return ",".join(cards)
    
    def print_sum_value(self):
        _sum_card_values = self.sum_card_values()
        self.print_cards()
        timing = Timing()
        timing.print_time(_sum_card_values, self.name)
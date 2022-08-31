from Timing import Timing
import re
from Card import Card

class CardPile:
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
            x = re.search("^\d+", card)
            sum = sum + int(x.group())
        return sum

    def sort_ascending(self):
        return sorted(self.cards)

    def sort_descending(self):
        return sorted(self.cards, reverse = True)

    def add_to_deck(self, deck):
        if(self.cards is not None):
            deck = self.deck + self.cards
            self.cards = []
        return deck  

    def remove_many_minutes(self, minutes):
        cards = self.sort_descending()
        for card in cards:
            if(minutes - Card.GetValue(card) > 0):
                cards.pop(0)        

    def print_cards(self):
        print(self.name + " pile: ", self.cards)
    
    def print_sum_value(self):
        _sum_card_values = self.sum_card_values()
        print('sum total of cards: ' + str(_sum_card_values))
        print(self.cards)

        timing = Timing()
        timing.print_time(_sum_card_values, self.name)
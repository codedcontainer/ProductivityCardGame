import random
import re
from Card import Card

class CardDeck:
    suits = ['h', 'd', 'c', 's']
    values = [str(val) for val in range(1,14)]
    cards = []

    def __init__(self):
        self.create()
        self.add_joker(2)
        self.shuffle(self.cards)

    def create(self):
        for value in self.values:
            for suit in self.suits:
                self.cards.append(str(value) + suit)
                #card = Card(value, suit)
                #self.cards.append(card)

    def add_joker(self, amount):
        for joker in range(1,amount+1):
            # card = Card(0, "j")
            # self.cards.append(card)
            self.cards.append('0j')
    
    def discard_joker(self):
        regex_j = re.search("j",self.cards[0])
        if(regex_j is not None):
            self.cards.pop(0)
        else:
            print("card "+ self.cards[0] + "is not a valid card")

    def shuffle(self,cards):
        card_count = len(cards)
        for card in enumerate(cards):
            index = card[0]
            value = card[1]
            random_int = random.randint(1,card_count-1)
            random_card = cards[random_int]
            cards[index] = random_card 
            cards[random_int] = value

    def draw(self):
        card = self.cards[0]
        self.cards.pop(0)
        return card

    def reset(self):
        self.cards = []
        self.create()
        self.add_joker(2)
        self.shuffle(self.cards)
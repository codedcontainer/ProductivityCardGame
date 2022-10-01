"Productivity card game"
from Model.CardDeck import CardDeck
from Model.CardPile import CardPile
from Model.DiscardPile import DiscardPile
from tkinter import messagebox

class CardGame:
    "Card game"
    def __init__(self):
        self.initialize()

    def initialize(self):
        "Setup piles"
        self.deck = CardDeck()
        self.piles = [DiscardPile(), CardPile("work"), CardPile("fun")]
        self.pileMap = {}

        for pile in self.piles:
            self.pileMap[pile.name] = pile

        self.suitToPileMap = {
            "s" : self.pileMap['work'],
            "c" : self.pileMap['work'],
            "h" : self.pileMap['fun'],
            "d" : self.pileMap['fun']
        }


    def draw(self):
        "Draw a card"
        if len(self.deck.cards) > 0:
            card = self.deck.draw()
            
            if card.suit == "j" :
                self.deck.discard_joker()
                self.deck.append_pile(self.pileMap['discard'])
                self.deck.shuffle()
            else:
                self.suitToPileMap[card.suit].cards.append(card)
        else:
            messagebox.showwarning(message="Cannot draw any more cards; deck is empty")

    def printPiles(self):
        "Print the the sum value of the piles"
        for pile in self.piles:
            pile.print_sum_value()

    def draw_to_pile_target(self, pile, time_target_min, adj_time_target):
        "Draw cards to a target value in minutes"
        pile_sum = pile.sum_card_values()
        
        if len(self.deck.cards) == 0 :
            messagebox.showwarning(message="Cannot draw any more cards; deck is empty")
            return
        if adj_time_target <= 0:
            if len(pile.cards) > 0:
                messagebox.showinfo(message="Target reached!")
                return
        if pile_sum >= time_target_min:
            return

        drawn_card = self.deck.draw()
        if drawn_card.suit == "j" :
                self.deck.discard_joker()
                self.deck.append_pile(self.pileMap['discard'])
                self.deck.shuffle()
        else:
            pile.add(drawn_card)

        return self.draw_to_pile_target(pile, time_target_min, time_target_min - int(drawn_card.value))
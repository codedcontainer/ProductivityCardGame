"Playing card discard pile"
from CardPile import CardPile

class DiscardPile(CardPile):
    "discard pile"
    def __init__(self):
        CardPile.__init__(self, "discard")

    def move_all_to_draw(self, deck):
        "move all cards to the draw pile"
        if self.cards is not None :
            deck.cards = deck.cards + self.cards
            self.cards = []
            deck.suffle()
            
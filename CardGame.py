"Productivity card game"

from CardDeck import CardDeck
from CardPile import CardPile
from DiscardPile import DiscardPile
import Console

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
            else:
                self.suitToPileMap[card.suit].cards.append(card)
        else:
            print("cannot draw any more cards; deck is empty")

    def printPiles(self):
        "Print the the sum value of the piles"
        for pile in self.piles:
            pile.print_sum_value()

    def draw_to_pile_target(self, pile, time_target_min):
        "Draw cards to a target value in minutes"
        pile_sum = pile.sum_card_values()
        if len(self.deck.cards) == 0 :
            print("cannot draw any more")
            return "Cannot draw any more cards from deck. The draw pile is empty"
        if time_target_min <= 0:
            if len(pile.cards) > 0:
                print('target reached')
                return "Target reached!"
        if pile_sum >= time_target_min:
            return "Target reached!"

        drawn_card = self.deck.draw()
        pile.add(drawn_card)
        return self.draw_to_pile_target(pile, time_target_min - int(drawn_card.value))

    def prompt_restart(self):
        "prompt to restart"
        restart = input("Would you like to restart the app (y/n)? ")
        if restart.lower() == "y":
            self.restart()

    def prompt_draw_single(self):
        "prompt to draw a single card"
        isDraw = input("Would you like to draw a single card? ")
        if isDraw.lower() == "n":
            Console.clear()
            self.prompt_draw_target()
        else:
            Console.clear()
            self.draw()
            self.printPiles()
            self.start()

    def prompt_draw_target(self):
        "prompt to draw to a target value in minutes"
        isDrawtoTarget = input("Would you like to draw to a target (y/n)? ")
        if isDrawtoTarget.lower() == "y" :
            pileName = input("Pile to add (work/fun)? ")
            pile = self.pileMap[pileName]
            time_target_minutes = int(input("Time target in minutes: "))
            if pile.sum_card_values() > 0:
                time_target_minutes = time_target_minutes - pile.sum_card_values()

            self.draw_to_pile_target(pile, time_target_minutes)
            self.start()
        else:
            self.remove_cards_target()

    def remove_cards_target(self):
        "prompt to remove cards by target value in minutes"
        isRemoveByTime = input("Would you like to remove cards by time spent (y/n)? ")
        if isRemoveByTime.lower() == "y" :
            pileName = input("Pile to discard cards (work/fun)?")
            pile = self.pileMap[pileName]
            time_target_minutes = int(input("Time spent in minutes: "))
            pile.remove_many_minutes(time_target_minutes)
            self.start()

    def start(self):
        "start game and begin prompts"
        self.prompt_draw_single()

    def restart(self):
        "restart game"
        self.initialize()
        self.start()

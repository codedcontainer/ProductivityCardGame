from CardDeck import CardDeck
from CardPile import CardPile
from DiscardPile import DiscardPile
import readline

class CardGame:
    def __init__(self):
        self.initialize()

    def initialize(self):
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
        if(len(self.deck.cards) > 0):
            card = self.deck.draw()
            if(card.suit == "j"):
                self.deck.discard_joker()
                print(self.pileMap['discard'])
                self.pileMap['discard'].move_all_to_draw()
            else:
                self.suitToPileMap[card.suit].cards.append(card)
        else:
            print("cannot draw any more cards; deck is empty")

    def draw_to_pile_target(self, pile, time_target_min):
        if(len(self.deck.cards) == 0 ):
            print("Cannot draw any more cards from deck. The draw pile is empty")
            pile.print_sum_value()
            self.prompt_restart()
        elif(time_target_min <= 0 and len(pile.cards) > 0):
            print("Target reached")
            pile.print_sum_value()
        else:
            drawn_card = self.deck.draw()            
            pile.add(drawn_card)   
            self.draw_to_pile_target(pile, time_target_min - int(drawn_card.value))

    def prompt_restart(self):
        restart = input("Would you like to restart the app (y/n)? ")
        if(restart.lower() == "y"):
            self.restart()

    def prompt_draw_single(self):
        readline.clear_history()
        isDraw = input("Would you like to draw a single card? ")
        if(isDraw.lower() == "n"):
            self.prompt_draw_target()
        else:            
            self.draw()
            self.pileMap['work'].print_sum_value()
            self.pileMap['fun'].print_sum_value()
            self.start()

    def prompt_draw_target(self):
        isDrawtoTarget = input("Would you like to draw to a target (y/n)? ")
        if(isDrawtoTarget.lower() == "y"):
            pileName = input("Pile to add (work/fun)? ")
            pile = self.pileMap[pileName]
            time_target_minutes = int(input("Time target in minutes: "))
            if(pile.sum_card_values() > 0):
                time_target_minutes = time_target_minutes - pile.sum_card_values()

            self.draw_to_pile_target(pile, time_target_minutes)  
            self.start()
        else:
            self.remove_cards_target()

    def remove_cards_target(self):
        isRemoveByTime = input("Would you like to remove cards by time spent (y/n)? ")
        if(isRemoveByTime.lower() == "y"):
            pileName = input("Pile to discard cards (work/fun)?")
            pile = self.pileMap[pileName]
            time_target_minutes = int(input("Time spent in minutes: ")) 
            pile.remove_many_minutes(time_target_minutes)
            self.start()

    def start(self):
       self.prompt_draw_single()

    def restart(self):
        self.initialize()
        self.start()
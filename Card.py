import re

class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    @staticmethod
    def GetSuit(cardStr):
        "Returns a cards suit"
        return re.search("\w$",cardStr).group()

    @staticmethod
    def GetValue(cardStr):
        "Retunrs a cards value"
        return re.search("\d+", cardStr).group()

    @staticmethod
    def AsString(card):
        "Returns a cards value and suit"
        return str(card.value) + card.suit

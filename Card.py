import re

class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    @staticmethod
    def GetSuit(cardStr):
        return re.search("\w$",cardStr).group()

    @staticmethod
    def GetValue(cardStr):
        return re.search("\d+", cardStr).group()
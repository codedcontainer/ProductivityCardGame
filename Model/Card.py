"""Playing card"""
import re


class Card:
    "Playing Card"
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    @staticmethod
    def get_suit(card_str):
        """Returns a cards suit"""
        return re.search("\w$", card_str).group()

    @staticmethod
    def get_value(card_str):
        """Returns a cards value"""
        return re.search("\d+", card_str).group()

    @staticmethod
    def as_string(card):
        """Returns a cards value and suit"""
        return str(card.value) + card.suit

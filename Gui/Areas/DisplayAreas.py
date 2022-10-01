"Shows all areas for display in tkinter app"
from Areas.PilesArea import PilesArea
from Areas.DiscardCardsArea import DiscardCardsArea
from Areas.DrawCardsArea import DrawCardsArea
from Areas.ResetArea import ResetArea

def DisplayAreas(card_game, tk):
    "Display all areas"
    pile_names = ["Work", "Fun"]
    PilesArea(tk)
    DiscardCardsArea(pile_names, card_game, tk)
    DrawCardsArea(pile_names, card_game, tk)

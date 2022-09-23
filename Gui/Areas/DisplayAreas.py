"Shows all areas for display in tkinter app"
from Gui.Areas.PilesArea import PilesArea
from Gui.Areas.DiscardCardsArea import DiscardCardsArea
from Gui.Areas.DrawCardsArea import DrawCardsArea
from Gui.Areas.ResetArea import ResetArea

def DisplayAreas(card_game, tk):
    "Display all areas"
    pile_names = ["Work", "Fun"]
    PilesArea(tk)
    DiscardCardsArea(pile_names, card_game, tk)
    DrawCardsArea(pile_names, card_game, tk)
    ResetArea(tk)

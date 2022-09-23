import sys
sys.path.append('../ProductivityCardGame')
from CardGame import CardGame

from tkinter import Tk
from Gui.Areas.DisplayAreas import DisplayAreas


tk = Tk()
tk.title("Productivity Card Game")

card_game = CardGame()
DisplayAreas(card_game, tk)

tk.mainloop()

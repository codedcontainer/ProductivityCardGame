"Inits tkinter gui window and starts card game"
import sys
from tkinter import Tk
from Areas.DisplayAreas import DisplayAreas
sys.path.append('../ProductivityCardGame')
from Model.CardGame import CardGame

tk = Tk()
tk.title("Productivity Card Game")

card_game = CardGame()
DisplayAreas(card_game, tk)

tk.mainloop()

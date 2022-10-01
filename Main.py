"""Inits tkinter gui window and starts card game"""
import sys
from tkinter import Tk
from tkinter import messagebox
sys.path.insert(0, '..')
from Areas.DisplayAreas import DisplayAreas
from Model.CardGame import CardGame

tk = Tk()
tk.title("Productivity Card Game")
tk.resizable(False, False)

card_game = CardGame(tk)
DisplayAreas(card_game, tk)

tk.mainloop()

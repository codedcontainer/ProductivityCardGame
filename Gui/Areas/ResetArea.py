"tkinter area to restart the game"
from tkinter import Button

def ResetArea(root):
    "Display area: reset game to starting state"
    reset_btn = Button(root, text="Reset game")
    reset_btn.grid(row=2, column=1)

from tkinter import Button

class ResetArea():
    "Display area: reset game to starting state"
    def __init__(self, root):
        self.root = root
        self.reset_game()

    def reset_game(self):
        "Display area: restart game"
        reset_btn = Button(self.root, text="Reset game")
        reset_btn.grid(row=2, column=1)
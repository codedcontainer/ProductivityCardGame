"tkinter area for drawing playing cards actions"
from tkinter import LabelFrame, Label, StringVar, Entry,OptionMenu, Button
from Commands import Commands

class DrawCardsArea():
    "Display area: draw cards from draw pile"
    def __init__(self, pile_names, card_game, rook):
        self.pile_names = pile_names
        self.card_game = card_game
        self.rook = rook
        self.dc_lf = LabelFrame(self.rook, text="Draw Cards")
        self.dc_lf.grid(row=1, column=2, padx=20, pady=20)

        self.draw_to_target()
        self.draw_card()

    def draw_card(self):
        "Dislay area: draw a single card button"
        draw_btn = Button(self.dc_lf, text="Draw a card",
                          command=lambda: Commands.draw(self.rook, self.card_game))
        draw_btn.grid(row=0, column=1, padx=10, pady=10)

    def draw_to_target(self):
        "Display area: draw cards to a target in minutes"
        dtt_lf = LabelFrame(self.dc_lf, text="By Target Time")
        dtt_lf.grid(row=0, column=0, padx=10, pady=10)

        dtt_lb = Label(dtt_lf, text="Target time(min):")
        dtt_lb.grid(row=1, column=0, padx=5, pady=5)
        self.rook.dtt_tb = Entry(dtt_lf)
        self.rook.dtt_tb.grid(row=2, column=0, padx=5, pady=(0,5))

        dtt_om_opts = self.pile_names
        self.rook.dtt_om_var = StringVar()
        self.rook.dtt_om_var.set(dtt_om_opts[0])

        dtt_om = OptionMenu(dtt_lf, self.rook.dtt_om_var, *dtt_om_opts)
        dtt_om.grid(row=3, column=0, padx=5, pady=5)

        dtt_btn = Button(dtt_lf, text="Draw to target",
                         command=lambda: Commands.draw_to_target(self.rook, self.card_game))
        dtt_btn.grid(row=4, column=0, padx=5, pady=(10,5))

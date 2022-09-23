from tkinter import LabelFrame, Label,Button, StringVar,OptionMenu, Entry
import sys
sys.path.append("../../ProductivityCardGame")
from Commands import Commands

class DiscardCardsArea():
    "Dispplay area: discard cards"
    def __init__(self, pile_names, card_game, tk):
        self.pile_names = pile_names
        self.card_game = card_game
        self.tk = tk

        self.dc_lf = LabelFrame(self.tk, text="Discard Cards")
        self.dc_lf.grid(row=1, column=1, padx=20, pady=20)
        self.remove_by_target()
        self.add_to_discard()

    def add_to_discard(self):
        "Display area: move cards to discard pile"
        atd_lf = LabelFrame(self.dc_lf, text="Move Pile To Discard")
        atd_lf.grid(row=0, column=2, padx=10, pady=10)

        atd_lb = Label(atd_lf, text="Pile to discard:")
        atd_lb.grid(row=1, column=2, padx=5, pady=5)

        atd_om_opts = self.pile_names
        self.tk.atd_om_var = StringVar()
        self.tk.atd_om_var.set(atd_om_opts[0])

        atd_om = OptionMenu(atd_lf, self.tk.atd_om_var, *atd_om_opts)
        atd_om.grid(row=2, column=2, padx=5, pady=5)

        atd_btn = Button(atd_lf, text="Discard pile",
                         command=lambda: Commands.discard_pile(self.tk, self.card_game))
        atd_btn.grid(row=3, column=2, padx=5, pady=(10,5))

    def remove_by_target(self):
        "Display area: remove cards from pile by target time"
        tbt_lf = LabelFrame(self.dc_lf, text="By Target Time")
        tbt_lf.grid(row=0, column=1, padx=10, pady=10)

        rft_lb = Label(tbt_lf, text="Target time(min):")
        rft_lb.grid(row=1, column=1, padx=5, pady=5)
        rft_tb = Entry(tbt_lf)
        rft_tb.grid(row=2, column=1,padx=5, pady=(0,5))

        rbt_om_opts = self.pile_names
        rbt_om_var = StringVar()
        rbt_om_var.set(rbt_om_opts[0])
        rbt_om = OptionMenu(tbt_lf, rbt_om_var, *rbt_om_opts)
        rbt_om.grid(row=3, column=1)

        rft_btn = Button(tbt_lf, text="Remove by target")
        rft_btn.grid(row=4, column=1,padx=5, pady=(10,5))

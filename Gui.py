from tkinter import *
from Commands import Commands
from CardGame import CardGame


root = Tk()
root.title("Productivity Card Game")

class Widgets:
    pile_names = ["Work", "Fun"]

    def __init__(self):
        self.cg = CardGame()

        self.alert()
        self.work_pile()
        self.fun_pile()        
        self.discard_pile()
        self.draw_to_target()
        self.remove_by_target()
        self.add_to_discard()
        self.draw_card()
        self.reset_game()        

    def alert(self):
        alert_label = Label(root)
        alert_label.pack()

    def work_pile(self):
        root.wp_label = Label(root, text="Work pile: ")
        root.wp_label.pack()

    def fun_pile(self):
        root.fp_label = Label(root, text="Fun pile: ")
        root.fp_label.pack()

    def discard_pile(self):
        root.dp_label = Label(root, text="Discard pile:")
        root.dp_label.pack()

    def add_to_discard(self):
        atd_lb = Label(root, text="Pile to discard:")
        atd_lb.pack()

        atd_om_opts = self.pile_names
        atd_om_var = StringVar()
        atd_om_var.set(atd_om_opts[0])

        atd_om = OptionMenu(root, atd_om_var, *atd_om_opts)
        atd_om.pack()

        atd_btn = Button(root, text="Discard pile")
        atd_btn.pack()

    def draw_to_target(self):
        dtt_lb = Label(root, text="Target time(min):")
        dtt_lb.pack()
        dtt_tb = Entry(root)
        dtt_tb.pack()

        dtt_om_opts = self.pile_names
        dtt_om_var = StringVar()
        dtt_om_var.set(dtt_om_opts[0])

        dtt_om = OptionMenu(root,dtt_om_var, *dtt_om_opts)
        dtt_om.pack()

        dtt_btn = Button(root, text="Draw to target")
        dtt_btn.pack()

    def remove_by_target(self):
        rft_lb = Label(root, text="Target time(min):")
        rft_lb.pack()
        rft_tb = Entry(root)
        rft_tb.pack()

        rbt_om_opts = self.pile_names
        rbt_om_var = StringVar()
        rbt_om_var.set(rbt_om_opts[0])
        rbt_om = OptionMenu(root,rbt_om_var, *rbt_om_opts)
        rbt_om.pack()

        rft_btn = Button(root, text="Remove by target")
        rft_btn.pack()

    def draw_card(self):
        draw_btn = Button(root, text="Draw a card", command=lambda: Commands.draw(root, self.cg))
        draw_btn.pack()

    def reset_game(self):
        reset_btn = Button(root, text="Reset game")
        reset_btn.pack()


Widgets()
root.mainloop()

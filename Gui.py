from tkinter import *

root = Tk()
root.title("Productivity Card Game")

class Widgets:
    pile_names = ["Work", "Fun"]

    def __init__(self):
        self.work_pile()
        self.fun_pile()
        self.discard_pile()
        self.draw_to_target()
        self.remove_by_target()
        self.draw_card()
        self.reset_game()        

    def work_pile(self):
        wp_label = Label(root, text="Work pile: ")
        wp_label.pack()

    def fun_pile(self):
        fp_label = Label(root, text="Fun pile: ")
        fp_label.pack()

    def discard_pile(self):
        fp_label = Label(root, text="Discard pile:")
        fp_label.pack()

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
        draw_btn = Button(root, text="Draw a card")
        draw_btn.pack()

    def reset_game(self):
        reset_btn = Button(root, text="Reset game")
        reset_btn.pack()


Widgets()
root.mainloop()

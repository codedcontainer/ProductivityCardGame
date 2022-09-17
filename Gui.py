from tkinter import *
from turtle import width
from Commands import Commands
from CardGame import CardGame


root = Tk()
root.title("Productivity Card Game")

class Widgets:
    pile_names = ["Work", "Fun"]

    def __init__(self):
        self.cg = CardGame()
        self.piles()
        self.draw_cards()
        self.discard_cards()     
        self.reset_game()    

    def piles(self):
        self.piles_lf = LabelFrame(root, text="Piles")
        self.piles_lf.grid(row=0, column=0, rowspan=2, padx=20, pady=20)
        self.work_pile()
        self.fun_pile()
        self.discard_pile()


    def draw_cards(self):
        self.dc_lf = LabelFrame(root, text="Draw Cards")
        self.dc_lf.grid(row=0,column=2)

        self.draw_to_target()
        self.draw_card()

    def draw_card(self):
        draw_btn = Button(self.dc_lf, text="Draw a card", command=lambda: Commands.draw(root, self.cg))
        draw_btn.grid(row=0, column=0)

    def draw_to_target(self):
        dtt_lf = LabelFrame(self.dc_lf, text="Draw Cards To Target Time")
        #dtt_lf.pack()

        dtt_lb = Label(dtt_lf, text="Target time(min):")
        #dtt_lb.pack()
        root.dtt_tb = Entry(dtt_lf)
        root.dtt_tb.pack()

        dtt_om_opts = self.pile_names
        root.dtt_om_var = StringVar()
        root.dtt_om_var.set(dtt_om_opts[0])

        dtt_om = OptionMenu(dtt_lf,root.dtt_om_var, *dtt_om_opts)
        #dtt_om.pack()

        dtt_btn = Button(dtt_lf, text="Draw to target", command=lambda: Commands.draw_to_target(root,self.cg))
         
    def work_pile(self):
        wp_lf = LabelFrame(self.piles_lf, text="Work Pile", padx=10, pady=10)
        wp_lf.grid(row=0, column=0, padx=10, pady=5)

        root.wp_label = Label(wp_lf)
        root.wp_label.grid(row=1, column=0)

        wp_l = Label(self.piles_lf, text="Sum: 1hr 30m")
        wp_l.grid(row=0, column=1)
    
    def fun_pile(self):
        fp_lf = LabelFrame(self.piles_lf, text="Fun Pile", padx=10, pady=10)
        fp_lf.grid(row=1, column=0, padx=10, pady=5)
        root.fp_label = Label(fp_lf)
        root.fp_label.grid(row=2, column=0)

        fp_l = Label(self.piles_lf, text="Sum: 1hr 30m ")
        fp_l.grid(row=1, column=1)

    def discard_pile(self):
        dp_lf = LabelFrame(self.piles_lf, text="Discard Pile", padx=10, pady=10)
        dp_lf.grid(row=2, column=0, padx=(10,5), pady=5)

        root.dp_label = Label(dp_lf)
        root.dp_label.grid(row=3, column=0)

        dp_l = Label(self.piles_lf, text="Sum: 1hr 30m")
        dp_l.grid(row=2, column=1, padx=10)

    def discard_cards(self):
        self.dc_lf = LabelFrame(root, text="Discard Cards")
        self.dc_lf.grid(row=0, column=1, padx=20, pady=20)
        self.remove_by_target()
        self.add_to_discard()      

    def add_to_discard(self):
        atd_lf = LabelFrame(self.dc_lf, text="Move Pile To Discard")
        atd_lf.grid(row=0, column=2, padx=10, pady=10)

        atd_lb = Label(atd_lf, text="Pile to discard:")
        atd_lb.grid(row=1, column=2)

        atd_om_opts = self.pile_names
        root.atd_om_var = StringVar()
        root.atd_om_var.set(atd_om_opts[0])

        atd_om = OptionMenu(atd_lf, root.atd_om_var, *atd_om_opts)
        atd_om.grid(row=2, column=2)

        atd_btn = Button(atd_lf, text="Discard pile", command=lambda: Commands.discard_pile(root,self.cg ))
        atd_btn.grid(row=3, column=2)
    

    def remove_by_target(self):
        tbt_lf = LabelFrame(self.dc_lf, text="By Target Time")
        tbt_lf.grid(row=0, column=1, padx=10, pady=10)

        rft_lb = Label(tbt_lf, text="Target time(min):")
        rft_lb.grid(row=1, column=1)
        rft_tb = Entry(tbt_lf)
        rft_tb.grid(row=2, column=1)

        rbt_om_opts = self.pile_names
        rbt_om_var = StringVar()
        rbt_om_var.set(rbt_om_opts[0])
        rbt_om = OptionMenu(tbt_lf,rbt_om_var, *rbt_om_opts)
        rbt_om.grid(row=3, column=1)

        rft_btn = Button(tbt_lf, text="Remove by target")
        rft_btn.grid(row=4, column=1)

   

    def reset_game(self):
        reset_btn = Button(root, text="Reset game")
        reset_btn.grid(row=2, column=1)


Widgets()
root.mainloop()

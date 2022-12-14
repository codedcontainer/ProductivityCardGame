"tkinter widget event handler methods"
import tkinter as tk
from tkinter import messagebox

class Commands:
    "Event handler methods"
    @staticmethod
    def print_piles(root, cg):
        "Display string array of card piles"
        root.wp_label["text"]= cg.pileMap['work'].print_cards()
        root.fp_label["text"]= cg.pileMap['leisure'].print_cards()
        root.dp_label["text"]= cg.pileMap['discard'].print_cards()

    @staticmethod
    def draw(root, cg):
        "Draw a card"
        cg.draw()
        Commands.print_piles(root, cg)
        Commands.set_sum_times(root, cg)

    @staticmethod
    def discard_pile(root, cg):
        "Add pile to discard pile"
        pile = root.atd_om_var.get().lower()
        cg.pileMap[pile].add_to_discard(cg.pileMap['discard'])
        Commands.print_piles(root,cg)
        Commands.set_sum_times(root, cg)

    @staticmethod
    def draw_to_target(root, cg):
        "Draw to target value"
        target_time = 0
        try:
            if(root.dtt_tb.get() != ""):
                target_time = int(root.dtt_tb.get())
        except ValueError:
            tk.messagebox.showinfo(message="Value must be an integer")
        
        pile = root.dtt_om_var.get().lower()
        pile = cg.pileMap[pile]
        cg.draw_to_pile_target(pile, target_time, target_time)
        Commands.print_piles(root,cg)
        Commands.set_sum_times(root, cg)

    @staticmethod
    def remove_to_target(root, cg):
        "Remove to target value"
        target_time = 0
        try:
            if(root.rft_tb.get() != ""):
                target_time = int(root.rft_tb.get())
        except ValueError:
            tk.messagebox.showinfo(message="Value must be an integer")
  
        pile = root.rbt_om_var.get().lower()
        pile = cg.pileMap[pile]
        cg.remove_to_pile_target(pile, target_time, root)
        Commands.print_piles(root,cg)
        Commands.set_sum_times(root,cg)

    @staticmethod
    def set_sum_times(root, cg):
        "Displays sum total time for each pile"
        root.wp_l["text"] = "Sum: " + cg.pileMap['work'].print_sum_value
        root.fp_l["text"] = "Sum: " + cg.pileMap['leisure'].print_sum_value
        root.dp_l["text"] = "Sum: " + cg.pileMap['discard'].print_sum_value

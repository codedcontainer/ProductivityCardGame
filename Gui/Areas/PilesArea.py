"tkinter area to display all pile's cards and sums"
from tkinter import LabelFrame, Label

class PilesArea:
    "Display area: piles"
    def __init__(self, root):
        self.root = root
        "Display area: piles"
        self.piles_lf = LabelFrame(self.root, text="Piles")
        self.piles_lf.grid(row=0, column=0, columnspan=3, padx=20, pady=20)
        self.work_pile()
        self.fun_pile()
        self.discard_pile()

    def work_pile(self):
        "Display area: work pile cards and sum"
        wp_lf = LabelFrame(self.piles_lf, text="Work Pile", padx=10, pady=10)
        wp_lf.grid(row=0, column=0, padx=10, pady=5)

        self.root.wp_label = Label(wp_lf)
        self.root.wp_label.grid(row=1, column=0)

        self.root.wp_l = Label(self.piles_lf, text="Sum: 0hr. 0min.")
        self.root.wp_l.grid(row=0, column=1)

    def fun_pile(self):
        "Display area: leisure area cards and sum"
        fp_lf = LabelFrame(self.piles_lf, text="Fun Pile", padx=10, pady=10)
        fp_lf.grid(row=1, column=0, padx=10, pady=5)
        self.root.fp_label = Label(fp_lf)
        self.root.fp_label.grid(row=2, column=0)

        self.root.fp_l = Label(self.piles_lf, text="Sum: 0hr. 0min.")
        self.root.fp_l.grid(row=1, column=1)

    def discard_pile(self):
        "Display area: discard pile cards and sum"
        dp_lf = LabelFrame(
            self.piles_lf, text="Discard Pile", padx=10, pady=10)
        dp_lf.grid(row=2, column=0, padx=(10, 5), pady=5)

        self.root.dp_label = Label(dp_lf)
        self.root.dp_label.grid(row=3, column=0)

        self.root.dp_l = Label(self.piles_lf, text="Sum: 0hr. 0min.")
        self.root.dp_l.grid(row=2, column=1, padx=10)

class Commands:
  
    @staticmethod
    def print_piles(root, cg):
        root.wp_label["text"]= "Work pile: " +cg.pileMap['work'].print_cards()
        root.fp_label["text"]= "Fun pile: " +cg.pileMap['fun'].print_cards()
        root.dp_label["text"]= "Discard pile: " +cg.pileMap['discard'].print_cards()

    @staticmethod
    def draw(root, cg):
        cg.draw()
        Commands.print_piles(root, cg)

    @staticmethod
    def discard_pile(root, cg)
        cg    
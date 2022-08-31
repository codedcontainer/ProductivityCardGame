import unittest
from CardPile import CardPile

class TestCardPile(unittest.TestCase):
    def setUp(self) -> None:
        self.pile = CardPile("work")
        self.pile.add("3h")
        self.pile.add("4s")
    
    def testPileSum(self):
        pile_sum = self.pile.sum_card_values()
        self.assertEqual(7, pile_sum)

if __name__ == '__main__':
    unittest.main()

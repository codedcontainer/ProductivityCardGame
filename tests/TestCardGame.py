import unittest
from CardGame import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = CardGame()

    def testDeckHasCardOnStart(self):
        self.assertGreater(len(self.game.deck.cards), 0)

if __name__ == '__main__':
    unittest.main()
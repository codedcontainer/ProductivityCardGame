"Tests the card game"
import unittest
from CardGame import CardGame

class TestCardGame(unittest.TestCase):
    "Tests: card game"
    def setUp(self) -> None:
        self.game = CardGame()

    def testDeckHasCardOnStart(self):
        "Test deck has card on start"
        self.assertGreater(len(self.game.deck.cards), 0)

if __name__ == '__main__':
    unittest.main()

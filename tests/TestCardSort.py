import unittest

class TestCardSort(unittest.TestCase):
    "Test card sorting"
    def test_sortUnordered(self):
        "test sort is unordered"
        cards = ["3h", "1d", "1h", "5c", "9s", "0j", "2h"]
        sorted_cards = sorted(cards)
        self.assertEqual("0j", sorted_cards[0])   
        self.assertEqual("9s", sorted_cards[len(sorted_cards)- 1])     

if __name__ == '__main__':
    unittest.main()

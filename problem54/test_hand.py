import unittest

from hand import PokerHand, value_wins

class TestValue(unittest.TestCase):
    def test_value_comparison(self):
        self.assertTrue(value_wins('K', '6'))
        self.assertTrue(value_wins('3', '2'))
        self.assertFalse(value_wins('8', 'J'))
        self.assertFalse(value_wins('A', 'A'))

class TestHand(unittest.TestCase):
    
    def test_contains_value(self):
        my_hand = PokerHand(['7C', '8C', '5C', 'QD', '6C'])
        self.assertTrue(my_hand.contains_value('7'))
        self.assertTrue(my_hand.contains_value('Q'))
        self.assertFalse(my_hand.contains_value('K'))

    def test_is_straight_from(self):
        hand1 = PokerHand(['AH', 'KH','QC', 'TS', 'JC'])
        self.assertTrue(hand1.is_straight_from('A'))
        self.assertFalse(hand1.is_straight_from('K'))
        hand2 = PokerHand(['TH', '9H','7C', '7S', '6C'])
        self.assertFalse(hand2.is_straight_from('T'))

    def test_is_straight(self):
        hand1 = PokerHand(['KH','QC', 'TS', 'JC','9H'])
        self.assertTrue(hand1.is_straight())
        self.assertEqual(hand1.is_straight(),'K')
        hand2 = PokerHand(['KH','QC', 'TS', '8C','9H'])
        self.assertEqual(hand2.is_straight(), None)

    def test_is_flush_of(self):
        hand1 = PokerHand(['AH', 'KH','QH', '2H', '3H'])
        self.assertTrue(hand1.is_flush_of('H'))
        self.assertFalse(hand1.is_flush_of('C'))

    def test_is_flush(self):
        hand1 = PokerHand(['AH', 'KH','QH', '2H', '3H'])
        self.assertTrue(hand1.is_flush())
        hand2 = PokerHand(['AH', 'KC','QH', '2H', '3H'])
        self.assertFalse(hand2.is_flush())

    def test_high_card(self):
        hand1 = PokerHand(['KH', 'KC','QH', '2H', '3H'])
        self.assertEqual(hand1.high_card(), 'KH')

    def test_four_of_a_kind(self):
        hand1 = PokerHand(['KH', 'KC','KS', '2H', 'KD'])
        self.assertEqual(hand1.is_four_of_kind(), 'K')
        hand1 = PokerHand(['KH', 'QC','KS', '2H', 'KD'])
        self.assertEqual(hand1.is_four_of_kind(), None)

if __name__ == '__main__':
    unittest.main()

# my_hand = PokerHand(['7C', '8C', '5C', 'QD', '6C'])
# print(my_hand.__contains_value('Q'))
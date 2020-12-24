from unittest import TestCase
from yahtzee import calculate_four_kind

class TestCalculateFourKind(TestCase):
    def test_calculate_four_kind_valid(self):
        expected = 16
        actual = calculate_four_kind([["2", "2", "2", "2", "6"]])
        self.assertEqual(expected, actual)


    def test_calculate_four_kind_valid_two(self):
        expected = 11
        actual = calculate_four_kind([["2", "2", "2", "2", "5"]])
        self.assertEqual(expected, actual)


    def test_calculate_four_kind_invalid_three_kind(self):
        expected = 0
        actual = calculate_four_kind([["5", "5", "5", "2", "1"]])
        self.assertEqual(expected, actual)

    def test_calculate_four_kind_invalid_yahtzee(self):
        expected = 0
        actual = calculate_four_kind([["5", "5", "5", "5", "5"]])
        self.assertEqual(expected, actual)


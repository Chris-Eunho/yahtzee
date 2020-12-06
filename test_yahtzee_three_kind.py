from unittest import TestCase
from yahtzee import calculate_three_kind

class TestCalculateThreeKind(TestCase):
    def test_calculate_Three_kind_valid_four_kind(self):
        expected = 13
        actual = calculate_three_kind(["2", "2", "2", "2", "6"])
        self.assertEqual(expected, actual)

    def test_calculate_Three_kind_valid_three_kind(self):
        expected = 19
        actual = calculate_three_kind(["2", "2", "2", "1", "6"])
        self.assertEqual(expected, actual)

    def test_calculate_Three_kind_valid_three_kind_two(self):
        expected = 16
        actual = calculate_three_kind(["2", "2", "2", "2", "6"])
        self.assertEqual(expected, actual)


    def test_calculate_Three_kind_valid_yahtzee(self):
        expected = 25
        actual = calculate_three_kind(["5", "5", "5", "5", "5"])
        self.assertEqual(expected, actual)

    def test_calculate_Three_kind_invalid(self):
        expected = 0
        actual = calculate_three_kind(["2", "3", "4", "1", "1"])
        self.assertEqual(expected, actual)

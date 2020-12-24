from unittest import TestCase
from yahtzee import calculate_large_straight


class TestCalculateLargeStraight(TestCase):
    def test_calculate_large_straight_valid(self):
        expected = 40
        actual = calculate_large_straight(["1", "2", "3", "4", "5"])

        self.assertEqual(expected, actual)

    def test_calculate_large_straight_valid_two(self):
        expected = 40
        actual = calculate_large_straight(["2", "3", "4", "5", "6"])

        self.assertEqual(expected, actual)

    def test_calculate_large_straight_small_straight(self):
        expected = 0
        actual = calculate_large_straight(["2", "3", "4", "5", "5"])

        self.assertEqual(expected, actual)

    def test_calculate_large_straight_wrong_case(self):
        expected = 0
        actual = calculate_large_straight(["1", "3", "4", "5", "5"])

        self.assertEqual(expected, actual)

    def test_calculate_large_straight_yahtzee(self):
        expected = 0
        actual = calculate_large_straight(["1", "1", "1", "1", "1"])

        self.assertEqual(expected, actual)

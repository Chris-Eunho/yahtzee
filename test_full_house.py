from unittest import TestCase
from yahtzee import calculate_full_house


class TestCalculateFullHouse(TestCase):
    def test_calculate_full_house_valid(self):
        expected = 25
        actual = calculate_full_house([["2", "2", "2", "5", "5"]])
        self.assertEqual(expected, actual)

    def test_calculate_full_house_valid_two(self):
        expected = 25
        actual = calculate_full_house([["2", "2", "5", "5", "5"]])
        self.assertEqual(expected, actual)

    def test_calculate_full_house_invalid(self):
        expected = 0
        actual = calculate_full_house(["2", "2", "2", "5", "6"])
        self.assertEqual(expected, actual)

    def test_calculate_full_house_invalid_two(self):
        expected = 0
        actual = calculate_full_house([["2", "3", "4", "5", "5"]])
        self.assertEqual(expected, actual)

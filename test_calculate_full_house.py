from unittest import TestCase
from yahtzee import calculate_full_house


class TestCalculateFullHouse(TestCase):
    def test_calculate_full_house_valid_full_house(self):
        expected = 25
        actual = calculate_full_house(["2", "2", "2", "5", "5"])
        self.assertEqual(expected, actual)

    def test_calculate_full_house_valid_full_house_mixed(self):
        expected = 25
        actual = calculate_full_house(["2", "5", "2", "5", "5"])
        self.assertEqual(expected, actual)

    def test_calculate_full_house_valid_full_house_mixed_two(self):
        expected = 25
        actual = calculate_full_house(["1", "3", "1", "3", "1"])
        self.assertEqual(expected, actual)

    def test_calculate_full_house_invalid_full_house(self):
        expected = 0
        actual = calculate_full_house(["2", "2", "2", "5", "6"])
        self.assertEqual(expected, actual)

    def test_calculate_full_house_invalid_full_house_straight(self):
        expected = 0
        actual = calculate_full_house(["2", "3", "4", "5", "6"])
        self.assertEqual(expected, actual)

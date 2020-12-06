from unittest import TestCase
from yahtzee import calculate_small_straight


class TestCalculateSmallStraight(TestCase):
    def test_calculate_small_straight_valid(self):
        expected = 30
        actual = calculate_small_straight(["2", "3", "4", "5", "5"])

        self.assertEqual(expected, actual)


class TestCalculateSmallStraight(TestCase):
    def test_calculate_small_straight_large_straight(self):
        expected = 30
        actual = calculate_small_straight(["2", "3", "4", "5", "6"])

        self.assertEqual(expected, actual)


class TestCalculateSmallStraight(TestCase):
    def test_calculate_small_straight_valid_five_kinds(self):
        expected = 30
        actual = calculate_small_straight(["1", "3", "4", "5", "6"])

        self.assertEqual(expected, actual)


class TestCalculateSmallStraight(TestCase):
    def test_calculate_small_straight_valid_four_kinds(self):
        expected = 30
        actual = calculate_small_straight(["1", "1", "2", "3", "4"])

        self.assertEqual(expected, actual)


class TestCalculateSmallStraight(TestCase):
    def test_calculate_small_straight_invalid_four_kinds(self):
        expected = 30
        actual = calculate_small_straight(["2", "3", "4", "6", "6"])

        self.assertEqual(expected, actual)


class TestCalculateSmallStraight(TestCase):
    def test_calculate_small_straight_invalid_three_kinds(self):
        expected = 30
        actual = calculate_small_straight(["1", "1", "1", "2", "3"])

        self.assertEqual(expected, actual)






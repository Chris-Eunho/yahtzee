from unittest import TestCase
from yahtzee import number_combo_converter


class TestNumberComboConverter(TestCase):
    def test_number_combo_converter_one(self):
        actual = number_combo_converter("1")
        expected = "Ones"
        self.assertEqual(expected, actual)

    def test_number_combo_converter_one(self):
        actual = number_combo_converter("5")
        expected = "Fives"
        self.assertEqual(expected, actual)

    def test_number_combo_converter_one(self):
        actual = number_combo_converter("10")
        expected = "Small straight"
        self.assertEqual(expected, actual)

    def test_number_combo_converter_one(self):
        actual = number_combo_converter("13")
        expected = "Yahtzee"
        self.assertEqual(expected, actual)

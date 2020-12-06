from unittest import TestCase
from yahtzee import is_list_inclusive


class TestIsListInclusive(TestCase):
    def test_is_list_inclusive_true_case(self):
        expected = True
        actual = is_list_inclusive(["1", "2", "3", "4", "5"], ["1", "2"])
        self.assertEqual(expected, actual)

    def test_is_list_inclusive_same_lists(self):
        expected = True
        actual = is_list_inclusive(["1", "2"], ["1", "2"])
        self.assertEqual(expected, actual)

    def test_is_list_inclusive_multiple_same_elements(self):
        expected = True
        actual = is_list_inclusive(["1", "2", "2", "4", "5"], ["1", "2", "2"])
        self.assertEqual(expected, actual)

    def test_is_list_inclusive_multiple_elements_false(self):
        expected = False
        actual = is_list_inclusive(["1", "2", "3", "4", "5"], ["1", "1"])
        self.assertEqual(expected, actual)

    def test_is_list_inclusive_wrong_element(self):
        expected = True
        actual = is_list_inclusive(["1", "2", "3", "4", "5"], ["1", "2", "6"])
        self.assertEqual(expected, actual)

    def test_is_list_inclusive_wrong_order(self):
        expected = True
        actual = is_list_inclusive(["1", "2"], ["1", "2", "3", "4", "5"])
        self.assertEqual(expected, actual)

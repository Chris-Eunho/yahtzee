from unittest import TestCase
from yahtzee import get_difference_list


class TestGetDifferenceList(TestCase):
    def test_get_difference_list_partial(self):
        actual = get_difference_list(['1', '2', '3', '4', '5'], ['1', '2', '3'])
        expected = ['4', '5']
        self.assertEqual(expected, actual)

    def test_get_difference_list_all(self):
        actual = get_difference_list(['1','2','3','4','5'], ['1','2','3','4','5'])
        expected = []
        self.assertEqual(expected, actual)

    def test_get_difference_list_nothing(self):
        actual = get_difference_list(['1','2','3','4','5'], [])
        expected = ['1','2','3','4','5']
        self.assertEqual(expected, actual)

    def test_get_difference_list_same_numbers(self):
        actual = get_difference_list(['1','1','1','3','3'], ['1','3','1'])
        expected = ['1', '3']
        self.assertEqual(expected, actual)

from unittest import TestCase
from unittest.mock import patch
from yahtzee import keep_dice
import io


class TestKeepDice(TestCase):

    @patch('builtins.input', side_effect=[None])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_dice_keep_none(self, mock_print, mock_input):
        expected = []
        actual = keep_dice(["1", "2", "3", "4", "5"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['123'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_dice_keep_three(self, mock_print, mock_input):
        expected = ["1", "2", "3"]
        actual = keep_dice(["1", "2", "3", "4", "5"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['12345'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_dice_keep_all(self, mock_print, mock_input):
        expected = ["1", "2", "3", "4", "5"]
        actual = keep_dice(["1", "2", "3", "4", "5"])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['11'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_dice_keep_wrong_input(self, mock_print, mock_input):
        expected = "Invalid Input. Enter dice from [1, 2, 3, 4, 5] without white spaces.\n" \
                   "e.g.)If you want to keep [3, 3], then enter \"33\"\n"
        keep_dice(["1", "2", "3", "4", "5"])
        self.assertEqual(expected, mock_print.getvalue())


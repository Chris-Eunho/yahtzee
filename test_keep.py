from unittest import TestCase
from unittest.mock import patch
from yahtzee import keep_dice
import io


class TestKeepDice(TestCase):

    @patch('builtins.input', side_effect=['232'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_dice_partial_keep(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': []}
        keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = ['2', '3', '2']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['232'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_dice_partial_keep_two(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': ['6', '5']}
        keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = ['2', '2', '3', '6', '5']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['22365'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_dice_all_keep(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': []}
        keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = ['2', '2', '3', '6', '5']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2265'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_dice_all_keep_two(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': ['3']}
        keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = ['2', '2', '3', '6', '5']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_dice_nothing(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': []}
        keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = []
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_keep_dice_nothing_two(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': ['6', '5']}
        keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = ['6', '5']
        self.assertEqual(expected, actual)

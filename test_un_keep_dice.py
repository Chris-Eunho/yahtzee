from unittest import TestCase
from unittest.mock import patch
from yahtzee import un_keep_dice
import io


class TestUnKeepDice(TestCase):

    @patch('builtins.input', side_effect=['232'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_un_keep_dice_partial_un_keep(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': ['2', '2', '3', '6', '5']}
        un_keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = ['6', '5']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_un_keep_dice_partial_un_keep_two(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '1', '3', '6', '3'], 'Keep': ['6', '5']}
        un_keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = ['6']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['26532'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_un_keep_dice_all_un_keep(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': ['2', '2', '3', '6', '5']}
        un_keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = []
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_un_keep_dice_no_un_keep(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': ['2', '2', '3', '6', '5']}
        un_keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = ['2', '2', '3', '6', '5']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_un_keep_dice_no_un_keep_two(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '1', '6', '4'], 'Keep': ['6', '4']}
        un_keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = ['6', '4']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['26532'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_un_keep_dice_all_un_keep(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': ['2', '2', '3', '6', '5']}
        un_keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = []
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_un_keep_dice_no_un_keep_two(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '1', '3', '6', '2'], 'Keep': ['2']}
        un_keep_dice(dice_dict)
        actual = dice_dict['Keep']
        expected = ['2']
        self.assertEqual(expected, actual)
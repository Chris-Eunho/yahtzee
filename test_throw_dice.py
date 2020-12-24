from unittest import TestCase
from unittest.mock import patch
from yahtzee import throw_dice
import io


class TestThrowDice(TestCase):

    # No keep
    @patch('random.randint', side_effect=[1, 2, 3, 4, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_throw_dice_no_keep(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': []}
        throw_dice(dice_dict)
        actual = dice_dict['All']
        expected = ['1', '2', '3', '4', '5']
        self.assertEqual(expected, actual)

    # keep_one_die
    @patch('random.randint', side_effect=[1, 2, 3, 4])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_throw_dice_keep_one_die(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': ['3']}
        throw_dice(dice_dict)
        actual = dice_dict['All']
        expected = ['3', '1', '2', '3', '4']
        self.assertEqual(expected, actual)

    # keep two dice
    @patch('random.randint', side_effect=[1, 2, 3])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_throw_dice_keep_two_dice(self, mock_print, mock_input):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': ["2", "2"]}
        throw_dice(dice_dict)
        actual = dice_dict['All']
        expected = ['2', '2', '1', '2', '3']
        self.assertEqual(expected, actual)

    # keep five dice
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_throw_dice_keep_five_dice(self, mock_print):
        dice_dict = {'All': ['2', '2', '3', '6', '5'], 'Keep': ['2', '2', '3', '6', '5']}
        actual = dice_dict['All']
        expected = ['2', '2', '3', '6', '5']
        self.assertEqual(expected, actual)

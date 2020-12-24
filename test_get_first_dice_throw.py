from unittest import TestCase
from unittest.mock import patch
from yahtzee import get_first_dice_throw
import io


class TestGetFirstDiceThrow(TestCase):
    @patch('random.randint', side_effect=[1, 2, 3, 4, 5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_first_dice_throw_straight(self, mock_print, mock_input):
        actual = get_first_dice_throw()
        expected = {'All': ['1', '2', '3', '4', '5'], 'Keep': []}
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1, 1, 1, 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_first_dice_throw_yahtzee(self, mock_print, mock_input):
        actual = get_first_dice_throw()
        expected = {'All': ['1', '1', '1', '1', '1'], 'Keep': []}
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1, 4, 4, 1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_first_dice_throw_full_house(self, mock_print, mock_input):
        actual = get_first_dice_throw()
        expected = {'All': ['1', '1', '4', '4', '1'], 'Keep': []}
        self.assertEqual(expected, actual)
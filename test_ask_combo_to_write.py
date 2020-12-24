from unittest import TestCase
from unittest.mock import patch
from yahtzee import ask_combo_to_write
import io


class TestAskComboToWrite(TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_combo_to_write_valid_input_not_written_not_yahtzee(self, mock_print, mock_input):
        score_sheet = {"name": "player_name", "Ones": " ", "Twos": 4, "Threes": 9, "Fours": 12, "Fives": 20, "Sixes": 18,
                       "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                       "Large straight": 40,
                       "Chance": 21, "Yahtzee": " ", "Yahtzee count": 0}
        dice_list = ['1', '1', '1', '1', '2']
        actual = ask_combo_to_write(dice_list, score_sheet)
        expected = 'Ones'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['14', 'd', '111', 'Twos', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_combo_to_write_invalid_input_not_written_not_yahtzee(self, mock_print, mock_input):
        score_sheet = {"name": "player_name", "Ones": 1, "Twos": " ", "Threes": 9, "Fours": 12, "Fives": 20,
                       "Sixes": 18,
                       "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                       "Large straight": 40,
                       "Chance": 21, "Yahtzee": " ", "Yahtzee count": 0}
        dice_list = ['1', '1', '1', '1', '2']
        actual = ask_combo_to_write(dice_list, score_sheet)
        expected = 'Twos'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1', '6', '4', '10', '3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_combo_to_write_valid_input_written_not_yahtzee(self, mock_print, mock_input):
        score_sheet = {"name": "player_name", "Ones": 1, "Twos": " ", "Threes": " ", "Fours": 12, "Fives": 20,
                       "Sixes": 18,
                       "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                       "Large straight": 40,
                       "Chance": 21, "Yahtzee": " ", "Yahtzee count": 0}
        dice_list = ['1', '1', '1', '1', '2']
        actual = ask_combo_to_write(dice_list, score_sheet)
        expected = 'Threes'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['13'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_combo_to_write_valid_input_not_written_yahtzee(self, mock_print, mock_input):
        score_sheet = {"name": "player_name", "Ones": 1, "Twos": " ", "Threes": " ", "Fours": 12, "Fives": 20,
                       "Sixes": 18,
                       "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                       "Large straight": 40,
                       "Chance": 21, "Yahtzee": " ", "Yahtzee count": 0}
        dice_list = ['1', '1', '1', '1', '1']
        actual = ask_combo_to_write(dice_list, score_sheet)
        expected = 'Yahtzee'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['13'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_combo_to_write_valid_input_non_zero_written_yahtzee(self, mock_print, mock_input):
        score_sheet = {"name": "player_name", "Ones": 1, "Twos": " ", "Threes": " ", "Fours": 12, "Fives": 20,
                       "Sixes": 18,
                       "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                       "Large straight": 40,
                       "Chance": 21, "Yahtzee": 50, "Yahtzee count": 1}
        dice_list = ['1', '1', '1', '1', '1']
        actual = ask_combo_to_write(dice_list, score_sheet)
        expected = 'Yahtzee'
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['13', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_combo_to_write_valid_input_zero_written_yahtzee(self, mock_print, mock_input):
        score_sheet = {"name": "player_name", "Ones": 1, "Twos": " ", "Threes": " ", "Fours": 12, "Fives": 20,
                       "Sixes": 18,
                       "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                       "Large straight": 40,
                       "Chance": 21, "Yahtzee": 0, "Yahtzee count": 0}
        dice_list = ['1', '1', '1', '1', '1']
        actual = ask_combo_to_write(dice_list, score_sheet)
        expected = 'Twos'
        self.assertEqual(expected, actual)
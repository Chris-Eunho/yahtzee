from unittest import TestCase
from yahtzee import write_yahtzee


class TestWriteYahtzee(TestCase):

    def test_write_yahtzee_valid_yahtzee_not_written(self):
        score_sheet = {"name": "player_name", "Ones": 1, "Twos": 4, "Threes": 9, "Fours": 12, "Fives": 20, "Sixes": 18,
                       "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                       "Large straight": 40,
                       "Chance": 21, "Yahtzee": " ", "Yahtzee count": 0}
        dice_list = ['1', '1', '1', '1', '1']
        write_yahtzee(dice_list, score_sheet)
        actual = [score_sheet["Yahtzee"], score_sheet["Yahtzee count"]]
        expected = [50, 1]
        self.assertEqual(expected, actual)

    def test_write_yahtzee_valid_yahtzee_written(self):
        score_sheet = {"name": "player_name", "Ones": 1, "Twos": 4, "Threes": 9, "Fours": 12, "Fives": 20, "Sixes": 18,
                       "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                       "Large straight": 40,
                       "Chance": 21, "Yahtzee": 50, "Yahtzee count": 1}
        dice_list = ['2', '2', '2', '2', '2']
        write_yahtzee(dice_list, score_sheet)
        actual = [score_sheet["Yahtzee"], score_sheet["Yahtzee count"]]
        expected = [150, 2]
        self.assertEqual(expected, actual)

    def test_write_yahtzee_invalid_yahtzee_not_written(self):
        score_sheet = {"name": "player_name", "Ones": 1, "Twos": 4, "Threes": 9, "Fours": 12, "Fives": 20, "Sixes": 18,
                       "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                       "Large straight": 40,
                       "Chance": 21, "Yahtzee": " ", "Yahtzee count": 0}
        dice_list = ['1', '1', '1', '2', '1']
        write_yahtzee(dice_list, score_sheet)
        actual = [score_sheet["Yahtzee"], score_sheet["Yahtzee count"]]
        expected = [0, 0]
        self.assertEqual(expected, actual)

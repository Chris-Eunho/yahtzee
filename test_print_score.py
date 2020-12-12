from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import print_score


class TestPrintScore(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_score_one(self, mock_print):
        expected = "<player_name's Score Sheet>\n\
                    [1]Ones: 1	[2]Twos: 4	[3]Threes: 9	[4]Fours: 12	[5]Fives: 20	[6]Sixes: 18\n\
                    [7]Three of a kind: 16	[8]Four of a kind: 23	[9]Full House: 25	[10]Small straight: 30\n\
                    [11]Large straight: 40	[12]Chance: 21	[13]Yahtzee: 0	**Yahtzee count: 0"

        sample = {"name": "player_name", "Ones": 1, "Twos": 4, "Threes": 9, "Fours": 12, "Fives": 20, "Sixes": 18,
                  "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                  "Large straight": 40,
                  "Chance": 21, "Yahtzee": 0, "Yahtzee count": 0}
        print_score(sample)
        self.assertEqual(expected, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_score_two(self, mock_print):
        expected = "<player_name's Score Sheet> \
                    [1]Ones: 1	[2]Twos: 4	[3]Threes: 9	[4]Fours: 12	[5]Fives: 10	[6]Sixes: 6 \
                    [7]Three of a kind: 10	[8]Four of a kind: 23	[9]Full House: 25	[10]Small straight: 30 \
                    [11]Large straight: 40	[12]Chance: 13	[13]Yahtzee: 50	**Yahtzee count: 0"

        sample = {"name": "player_name", "Ones": 1, "Twos": 4, "Threes": 9, "Fours": 12, "Fives": 10, "Sixes": 6,
                  "Three of a kind": 10, "Four of a kind": 23, "Full House": 25, "Small straight": 30,
                  "Large straight": 40,
                  "Chance": 13, "Yahtzee": 50, "Yahtzee count": 0}
        print_score(sample)
        self.assertEqual(expected, mock_print.getvalue())
from unittest import TestCase
from unittest.mock import patch
from yahtzee import ask_action
import io


class TestAskQuestion(TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_action_right_input(self, mock_print, mock_input):
        expected = '1'
        actual = ask_action()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_action_right_input_two(self, mock_print, mock_input):
        expected = '2'
        actual = ask_action()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_action_right_input_three(self, mock_print, mock_input):
        expected = '3'
        actual = ask_action()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['a', ' ', '4', '0', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_action_wrong_inputs(self, mock_print, mock_input):
        expected = '1'
        actual = ask_action()
        self.assertEqual(expected, actual)

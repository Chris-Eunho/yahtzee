from unittest import TestCase
from unittest.mock import patch
from yahtzee import ask_combo_to_write
import io


class TestAskComboToWrite(TestCase):

    @patch('builtins.input', side_effect=['123'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ask_combo_to_write(self, mock_print, mock_input):


        self.fail()

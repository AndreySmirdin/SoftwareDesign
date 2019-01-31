import unittest
from unittest.mock import patch

from src.reader import Reader


class ReaderTestCase(unittest.TestCase):

    def test_get_input_stacks_processed_input_correctly(self):
        self._run_reader(['echo 123'], 'echo 123')

    def test_multiline_input(self):
        self._run_reader(['echo \'123', '\"239', '\"', '\''],
                         'echo \'123\n\"239\n\"\n\'')

    def test_pipe(self):
        self._run_reader(['cat file.txt |', 'exit'],
                         'cat file.txt |\nexit')

    def _run_reader(self, user_input, expected_result):
        with patch('builtins.input', side_effect=user_input):
            stacks = Reader.read()
        self.assertEqual(stacks, expected_result)

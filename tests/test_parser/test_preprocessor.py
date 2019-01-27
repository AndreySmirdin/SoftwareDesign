import unittest

from src.parser.parsing_utils import find_symbols_not_in_quotes, find_unescaped_symbols


class PreprocessorTestCase(unittest.TestCase):

    def test_find_unescaped_symbols(self):
        result = find_unescaped_symbols('echo \'$a\'$a\'$a\'', '$')
        self.assertEqual(result, [9])
        result = find_unescaped_symbols('echo \"$a\'$a\'$a\"', '$')
        self.assertEqual(result, [6, 9, 12])

    def test_find_symbols_not_in_quotes(self):
        result = find_symbols_not_in_quotes('echo "$a" world " "', ' ')
        self.assertEqual(result, [4, 9, 15])

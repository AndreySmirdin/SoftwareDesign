import unittest

from src.parser.parsing_utils import Preprocessor


class PreprocessorTestCase(unittest.TestCase):

    def test_preprocessor_single_quotes(self):
        preprocessor = Preprocessor()
        result = preprocessor.find_unescaped_symbols('echo \'$a\'$a\'$a\'')
        self.assertEqual(result, [9])

    def test_preprocessor_double_quotes(self):
        preprocessor = Preprocessor()
        result = preprocessor.find_unescaped_symbols('echo \"$a\'$a\'$a\"')
        self.assertEqual(result, [6, 9, 12])

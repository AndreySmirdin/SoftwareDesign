import unittest

from src.parser.splitter import SplitterIntoCommands


class SplitterTestCase(unittest.TestCase):
    splitter = SplitterIntoCommands()

    def test_simple(self):
        self.assertEqual([['echo', 'a', 'b', 'c']], self.splitter.split_into_commands("echo a b c"))

    def test_with_quotes(self):
        self.assertEqual([['echo', '\"a b\"', 'c']], self.splitter.split_into_commands("echo \"a b\" c"))

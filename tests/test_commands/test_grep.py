import unittest

from src.commands.grep import Grep
from tests.test_commands.create_tmp_file import CreateTmpFile


class GrepTestCase(unittest.TestCase):
    text = '\n'.join(['Hello',
                      'hell',
                      'helloworld'])
    tmp_file = 'tmp.txt'

    @CreateTmpFile(tmp_file, text)
    def test_grep_without_keys(self):
        self.assertEqual('helloworld', Grep.run(['hello', 'tmp.txt'], None))

    @CreateTmpFile(tmp_file, text)
    def test_grep_with_ignore_case(self):
        self.assertEqual('Hello\nhelloworld', Grep.run(['-i', 'hello', 'tmp.txt'], None))

    @CreateTmpFile(tmp_file, text)
    def test_grep_with_whole_words(self):
        self.assertEqual('hell', Grep.run(['-w', 'hell', 'tmp.txt'], None))

    @CreateTmpFile(tmp_file, text)
    def test_grep_with_additional_lines(self):
        self.assertEqual('Hello\nhell', Grep.run(['-A 1', 'Hell', 'tmp.txt'], None))
        self.assertEqual('Hello\nhell\nhelloworld', Grep.run(['-A 2', 'Hell', 'tmp.txt'], None))

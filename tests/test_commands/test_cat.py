import unittest

from src.commands.cat import Cat
from tests.test_commands.create_tmp_file import CreateTmpFile


class WcTestCase(unittest.TestCase):
    text = 'Hello world'
    tmp_file = 'tmp.txt'

    @CreateTmpFile(tmp_file, text)
    def test_cat(self):
        self.assertEqual(self.text, Cat.run([self.tmp_file], None))

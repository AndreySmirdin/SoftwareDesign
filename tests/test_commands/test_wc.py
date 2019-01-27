import unittest

from src.commands.wc import Wc
from tests.test_commands.create_tmp_file import CreateTmpFile


class WcTestCase(unittest.TestCase):
    text = 'Hello world'
    tmp_file = 'tmp.txt'

    @CreateTmpFile(tmp_file, text)
    def test_wc(self):
        self.assertEqual((1, 2, 11), Wc.run([self.tmp_file], None))
        self.assertEqual((1, 2, 11), Wc.run([], self.tmp_file))

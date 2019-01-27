import unittest

from src.commands.external_command import ExternalCommand
from tests.test_commands.create_tmp_file import CreateTmpFile


class WcTestCase(unittest.TestCase):
    text = 'Hello world'
    tmp_file = 'tmp.txt'

    @CreateTmpFile(tmp_file, text)
    def test_cat(self):
        self.assertEqual(self.text, ExternalCommand.run(['cat', self.tmp_file], None))

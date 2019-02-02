import unittest

from src.commands.external_command import ExternalCommand
from tests.test_commands.create_tmp_file import CreateTmpFile


class ExternalCommandTestCase(unittest.TestCase):
    text = 'Hello world'
    tmp_file = 'tmp.txt'

    @CreateTmpFile(tmp_file, text)
    def test_with_external_cat(self):
        self.assertEqual("123", ExternalCommand.run(['cat', self.tmp_file], None))

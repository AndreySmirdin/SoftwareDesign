import unittest

from src.commands.external_command import ExternalCommand


class ExternalCommandTestCase(unittest.TestCase):
    def test_with_git(self):
        self.assertIn("repository", ExternalCommand.run(['git', 'help'], None))

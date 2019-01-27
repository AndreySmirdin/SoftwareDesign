import unittest

from src.commands.echo import Echo


class EchoTestCase(unittest.TestCase):

    def test_echo(self):
        self.assertEqual('1 2 3', Echo.run(['1', '2', '3'], None))
        self.assertEqual('"hello"', Echo.run(['"hello"'], None))

import unittest
import os

from src.commands.pwd import Pwd


class EchoTestCase(unittest.TestCase):

    def test_pwd(self):
        self.assertEqual(os.getcwd(), Pwd.run(None, None))

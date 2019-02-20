import unittest
import os

from src.commands.ls import Ls


class LsTestCase(unittest.TestCase):

    def test_ls(self):
        Ls.run("/", None)
        self.assertNotEqual(os.getcwd(), Ls.run(None, None))

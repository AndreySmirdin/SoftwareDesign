import unittest
import os

from src.commands.ls import Ls


class LsTestCase(unittest.TestCase):

    def test_ls(self):
        self.assertEqual('\n'.join(os.listdir(".")), Ls.run(None, None))
        self.assertEqual('\n'.join(os.listdir("/")), Ls.run("/", None))

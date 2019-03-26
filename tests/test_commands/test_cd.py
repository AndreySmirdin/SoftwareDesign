import unittest
import os

from src.commands.cd import Cd


class CdTestCase(unittest.TestCase):

    def test_cd(self):
        path = os.path.dirname(os.path.realpath(__file__))
        Cd.run("/", None)
        self.assertEqual("/", os.getcwd())
        Cd.run(path, None)
        self.assertEqual(path, os.getcwd())




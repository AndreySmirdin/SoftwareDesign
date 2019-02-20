import unittest
import os

from src.commands.cd import Cd


class CdTestCase(unittest.TestCase):

    def test_cd(self):
        path = os.getcwd()
        Cd.run("/", None)
        self.assertNotEqual(os.getcwd(), path)

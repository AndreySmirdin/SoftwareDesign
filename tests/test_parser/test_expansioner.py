import unittest

from src.parser.expansioner import Expansioner


class ExpansionerTestCase(unittest.TestCase):
    expansioner = Expansioner({'a': 'ex',
                               'b': 'it',
                               'c': '239',
                               'hello': 'world'})

    def test_simple(self):
        self.assertEqual('exit', self.expansioner.do_all_expansions('$a$b'))

    def test_with_double_quotes(self):
        self.assertEqual('"world  239', self.expansioner.do_all_expansions('"$hello"  $c'))

    def test_with_sinle_quptes(self):
        self.assertEqual('"world  \'$c\'', self.expansioner.do_all_expansions('"$hello"  \'$c\''))

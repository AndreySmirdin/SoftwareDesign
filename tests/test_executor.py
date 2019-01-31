import unittest

from src.commands.external_command import ExternalCommandException
from src.executor import Executor


class ExecutorTestCase(unittest.TestCase):
    executor = Executor({})

    def test_execute_implemented_command(self):
        result = self.executor.execute([['echo', 'hello']])
        self.assertEqual((True, 'hello'), result)

    def test_exit_command(self):
        result = self.executor.execute([['echo', 'hello'], ['exit']])
        self.assertEqual((False, None), result)

    def test_external_command(self):
        _, result = self.executor.execute([['git', 'help']])
        self.assertIn('repository', result)

    def test_unexisting_command(self):
        with self.assertRaises(ExternalCommandException):
            self.executor.execute([['abrval']])

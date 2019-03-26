import os

from src.commands.abstract_command import AbstractCommand


class Cd(AbstractCommand):
    """
    Cd command.
    """
    name = 'cd'

    @classmethod
    def run(cls, args, stdin):
        if not args:
            args = [os.path.expanduser("~")]
        if isinstance(args, str):
            args = [args]
        os.chdir(args[0])

import os

from src.commands.abstract_command import AbstractCommand


class Cd(AbstractCommand):
    """
    Cd command.
    """
    name = 'cd'

    @classmethod
    def run(cls, args, stdin):
        os.chdir(args[0])

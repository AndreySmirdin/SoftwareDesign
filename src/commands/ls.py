import os

from src.commands.abstract_command import AbstractCommand


class Ls(AbstractCommand):
    """
    Ls command.
    """
    name = 'ls'

    @classmethod
    def run(cls, args, stdin):
        print(os.listdir().join('\n'))

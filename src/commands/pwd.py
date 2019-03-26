import os

from src.commands.abstract_command import AbstractCommand


class Pwd(AbstractCommand):
    """
    Pwd command.
    """
    name = 'pwd'

    @classmethod
    def run(cls, args, stdin):
        return os.getcwd()

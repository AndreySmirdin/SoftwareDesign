import os

from src.commands.abstract_command import AbstractCommand


class Ls(AbstractCommand):
    """
    Ls command.
    """
    name = 'ls'

    @classmethod
    def run(cls, args, stdin):
        if isinstance(args, str):
            args = [args]
        if not args:
            args = [None]
        res = []
        for arg in args:
            res.append(Ls.__one_arg(arg))
        return '\n'.join(res)

    @staticmethod
    def __one_arg(args):
        return '\n'.join(os.listdir(args))

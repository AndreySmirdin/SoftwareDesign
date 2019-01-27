import os

from src.commands.abstract_command import AbstractCommand


class Pwd(AbstractCommand):
    name = 'pwd'

    @classmethod
    def run(cls, args, stdin):
        print(os.getcwd())

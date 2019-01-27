from src.commands.abstract_command import AbstractCommand


class Echo(AbstractCommand):
    name = 'echo'

    @classmethod
    def run(cls, args, stdin):
        return " ".join(args)

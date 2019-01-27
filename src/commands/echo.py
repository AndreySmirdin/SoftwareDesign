from src.commands.abstract_command import AbstractCommand


class Echo(AbstractCommand):
    """
    Printing all given arguments.
    """
    name = 'echo'

    @classmethod
    def run(cls, args, stdin):
        return " ".join(args)

from src.commands.abstract_command import AbstractCommand


class Cat(AbstractCommand):
    """
    Simple cat that prints file that was given as it's first argument.
    """

    name = 'cat'

    @classmethod
    def run(cls, args, stdin):
        if args:
            with open(args[0], 'r') as file:
                return ''.join(file.readlines())
        else:
            return stdin

from src.commands.abstract_command import AbstractCommand


class Wc(AbstractCommand):
    """
    Wc command that counts stat for the file that was given as first argument.
    """
    name = 'wc'

    @classmethod
    def run(cls, args, stdin):
        data = stdin
        if args:
            with open(args[0], 'r') as file:
                data = file.read()

        lines = data.count('\n') + 1
        words = len(data.split(None))
        chars = len(data)

        return '    {0}    {1}    {2}'.format(lines, words, chars)

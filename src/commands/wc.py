from src.commands.abstract_command import AbstractCommand


class Wc(AbstractCommand):
    name = 'wc'

    @classmethod
    def run(cls, args, stdin):
        file_name = args[0] if args else stdin
        with open(file_name, 'r') as file:
            lines = 0
            words = 0
            chars = 0
            for line in file:
                lines += 1
                words += len(line.split(' '))
                chars += len(line)

        return lines, words, chars

import argparse
import re

from src.commands.abstract_command import AbstractCommand


class Grep(AbstractCommand):
    """
    Grep command that supports -i, -w and -A NUM keys (they behave the way they do in bash).
    """
    name = 'grep'

    @classmethod
    def run(cls, args, stdin):
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument('-i', action='store_true', help='Ignore case distinctions')
        parser.add_argument('-w', action='store_true',
                            help='Select only those lines containing matches that form whole words.')
        parser.add_argument('-A', metavar='NUM', type=int,
                            help='Print NUM lines of trailing context after matching lines.')

        parser.usage = "grep [options] pattern [file]"

        try:
            known_args, unknown_args = parser.parse_known_args(args)
        except argparse.ArgumentError:
            raise ValueError("grep: invalid arguments\n" + parser.format_help())
        except SystemExit:
            return

        pattern = unknown_args[0]

        if len(unknown_args) > 2:
            raise ValueError("grep: Too many arguments.\n" + parser.format_help())
        if len(unknown_args) > 1:
            with open(unknown_args[1], 'r') as file:
                data = file.read().split('\n')
        elif stdin is not None:
            data = stdin.split('\n')
        else:
            raise ValueError("grep: no file to look\n" + parser.format_help())

        grep_args = re.IGNORECASE if known_args.i else 0

        if known_args.w:
            pattern = r'\b' + pattern + r'\b'

        strings_after = 0 if known_args.A is None else known_args.A

        if strings_after < 0:
            raise ValueError("grep: -A should be a non-negative integer. You provided {}.".format(strings_after))

        compiled_pattern = re.compile(pattern, grep_args)
        in_result = [False for _ in range(len(data))]
        for i in range(len(data)):
            if re.search(compiled_pattern, data[i]):
                for j in range(strings_after + 1):
                    if i + j < len(data):
                        in_result[i + j] = True
        result = []
        for (i, line) in enumerate(data):
            if in_result[i]:
                result.append(line)
        return '\n'.join(result)

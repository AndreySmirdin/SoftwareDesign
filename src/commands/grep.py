import argparse
import re

from src.commands.abstract_command import AbstractCommand


class Grep(AbstractCommand):
    name = 'grep'

    @classmethod
    def run(cls, args, stdin):
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', action='store_true', help='Ignore case distinctions')
        parser.add_argument('-w', action='store_true',
                            help=' Select  only those lines containing matches that form whole words.')
        parser.add_argument('-A', type=int,
                            help='An optional integer argument')

        known_args = None
        unknown_args = []
        try:
            known_args, unknown_args = parser.parse_known_args(args)
        except Exception as e:
            pass

        pattern = unknown_args[0]
        data = ''
        if len(unknown_args) > 1:
            with open(unknown_args[1], 'r') as file:
                data = file.read().split('\n')
        elif stdin is not None:
            data = stdin.split('\n')

        grep_args = re.IGNORECASE if known_args.i else 0

        if known_args.w:
            pattern = r'\b' + pattern + r'\b'

        strings_after = 0 if known_args.A is None else known_args.A

        compiled_pattern = re.compile(pattern, grep_args)
        result = []
        i = 0
        while i < len(data):
            if re.search(compiled_pattern, data[i]):
                result.append(data[i])
                result.extend(data[i + 1: i + strings_after + 1])
                i += strings_after
            i += 1

        return '\n'.join(result)

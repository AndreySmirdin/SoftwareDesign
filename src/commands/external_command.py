import subprocess

from src.commands.abstract_command import AbstractCommand


class ExternalCommand(AbstractCommand):
    @classmethod
    def name(cls):
        return ''

    @classmethod
    def run(cls, args, stdin):
        if stdin:
            with open(stdin, 'r') as f:
                data = f.readlines()
        else:
            data = None

        try:
            result = subprocess.run(args, check=True, stdin=data, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            raise IOError

import subprocess

from src.commands.abstract_command import AbstractCommand


class ExternalCommand(AbstractCommand):
    @classmethod
    def name(cls):
        return ''

    @classmethod
    def run(cls, args, stdin):
        try:
            result = subprocess.run(args, check=True, stdin=stdin, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            raise IOError

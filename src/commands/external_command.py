import subprocess

from src.commands.abstract_command import AbstractCommand


class ExternalCommand(AbstractCommand):
    """
    Calling an external command.
    """
    @classmethod
    def name(cls):
        return ''

    @classmethod
    def run(cls, args, stdin):
        try:
            result = subprocess.run(args, check=True, stdin=stdin, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            raise ExternalCommandException(e.stderr.decode('utf-8'))
        except FileNotFoundError:
            raise ExternalCommandException(args[0] + ": command not found")


class ExternalCommandException(Exception):

    def __init__(self, message):
        self.message = message

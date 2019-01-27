import re

from src.commands.cat import Cat
from src.commands.echo import Echo
from src.commands.external_command import ExternalCommand
from src.commands.pwd import Pwd
from src.commands.wc import Wc


class Executor(object):
    ASSIGNMENT_PATTERN = re.compile('[a-zA-Z]+?=\w*')

    EXIT = 'exit'

    SUPPORTED_COMMANDS = [Echo,
                          Cat,
                          Wc,
                          Pwd]

    def __init__(self, variables):
        self.variables = variables

    def execute(self, commands):
        if len(commands) == 1 and len(commands[0]) == 1 and re.match(self.ASSIGNMENT_PATTERN, commands[0][0]):
            splitted = commands[0][0].split('=', 1)
            self.variables[splitted[0]] = splitted[1]
            return True, None

        previous_output = None
        for command in commands[:-1]:
            should_continue, previous_output = self._call_command(command, previous_output)
            if not should_continue:
                return False, None

        return self._call_command(commands[-1], previous_output)

    def _call_command(self, command, input_file):
        if command[0] == self.EXIT:
            return False, None

        for supported_command in self.SUPPORTED_COMMANDS:
            if command[0] == supported_command.name:
                return True, supported_command.run(command[1:], input_file)

        return True, ExternalCommand.run(command, input_file)

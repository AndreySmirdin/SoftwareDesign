import re
import sys

from src.commands.cat import Cat
from src.commands.echo import Echo
from src.commands.external_command import ExternalCommand
from src.commands.pwd import Pwd
from src.commands.wc import Wc


class Executor(object):
    ASSIGNMENT_PATTERN = re.compile('[a-zA-Z]+?=\b')
    FILE_FOR_PIPE_1 = 'tmp_pipeline_file_1.txt'
    FILE_FOR_PIPE_2 = 'tmp_pipeline_file_2.txt'

    SUPPORTED_COMMANDS = [Echo,
                          Cat,
                          Wc,
                          Pwd]

    def __init__(self, variables):
        self.variables = variables

    def execute(self, commands):
        if len(commands) == 1 and len(commands[0]) == 1 and re.match(self.ASSIGNMENT_PATTERN, commands[0][0]):
            self.variables = commands[0][0].split('=', 1)[1]
            return True

        input_file = self.FILE_FOR_PIPE_1
        output_file = self.FILE_FOR_PIPE_2
        for command in commands[:-1]:
            sys.stdout = open(output_file, "w")
            if not self.call_command(command[-1], input_file):
                return False
            sys.stdout = sys.__stdout__

            input_file, output_file = output_file, input_file

        return self.call_command(commands[-1], input_file)

    def call_command(self, command, input_file):
        for supported_command in self.SUPPORTED_COMMANDS:
            if command[0] == supported_command.name:
                supported_command.run(command[1:], input_file)
                return True

        if command[0] == 'exit':
            return False

        ExternalCommand.run(command[1:], input_file)
        return True

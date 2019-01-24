from src.parser.parser import Parser
from src.reader import Reader


class Interpreter(object):

    def __init__(self):
        self.variables = {}
        self.parser = Parser()

    def run(self):
        user_input = Reader.read()
        commands = self.parser.parse(user_input)

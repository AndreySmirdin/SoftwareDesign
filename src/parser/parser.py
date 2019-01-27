from src.parser.expansioner import Expansioner
from src.parser.parsing_utils import remove_quotes
from src.parser.splitter import SplitterIntoCommands


class Parser(object):

    def __init__(self, variables):
        self.expansioner = Expansioner(variables)

    def parse(self, user_input):
        expansioned = self.expansioner.do_all_expansions(user_input)
        commands = SplitterIntoCommands.split_into_commands(expansioned)
        return remove_quotes(commands)

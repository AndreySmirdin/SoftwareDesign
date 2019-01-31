from src.parser.expansioner import Expansioner
from src.parser.parsing_utils import remove_quotes
from src.parser.splitter import SplitterIntoCommands


class Parser(object):
    """
    Class that connects all stages of parsing.
    """

    def __init__(self, variables):
        """
        :param variables: Dictionary with variables.
        """
        self.expansioner = Expansioner(variables)

    def parse(self, user_input):
        """
        Function that does all parsing.
        :param user_input: input.
        :return: list of commands splitted into words.
        """
        expansioned = self.expansioner.do_all_expansions(user_input)
        commands = SplitterIntoCommands.split_into_commands(expansioned)
        return remove_quotes(commands)

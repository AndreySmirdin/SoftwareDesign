import os

from src.parser.parsing_utils import find_unescaped_symbols


class Expansioner(object):
    """
    Class that is responsible for performing all expansions for a given input.
    """

    def __init__(self, variables):
        """
        :param variables: Dictionary with variables.
        """
        self.variables = variables

    def do_all_expansions(self, user_input):
        """
        Performing all expansions. By now only variables are replaced.
        :param user_input: input
        :return: string where all expansions were made.
        """
        return self._perform_variables_expansion(user_input)

    def _perform_variables_expansion(self, user_input):
        unescaped_dollars = find_unescaped_symbols(user_input, ['$'])
        result = ""
        i = 0
        while i < len(user_input):
            if user_input[i] == '$' and i in unescaped_dollars:
                name = ""
                i += 1
                while i < len(user_input) and user_input[i] not in ['\'', '\"', ' ', '\t', '\n', '$']:
                    name += user_input[i]
                    i += 1
                value = self.variables.get(name, '')
                result += value if value else os.environ.get(name, '')
            else:
                result += user_input[i]
                i += 1

        return result

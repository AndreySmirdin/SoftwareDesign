from src.parser.parsing_utils import find_unescaped_symbols


class Expansioner(object):
    def __init__(self, variables):
        self.variables = variables

    def do_all_expansions(self, user_input):
        return self._perform_variables_expansion(user_input)

    def _perform_variables_expansion(self, user_input):
        unescaped_dollars = find_unescaped_symbols(user_input, ['$'])
        result = ""
        i = 0
        while i < len(user_input):
            if user_input[i] == '$' and user_input[i] in unescaped_dollars:
                name = ""
                while i < len(user_input) and user_input[i] not in ['\'', '\"', ' ']:
                    name += user_input[i]
                    i += 1
                result += self.variables.get(name, '')
            i += 1

        return result

class Expansioner(object):
    def __init__(self, variables):
        self.variables = variables

    def perform_variables_expansion(self, user_input, unescaped_characters):
        result = ""
        i = 0
        while i < len(user_input):
            if user_input[i] == '$' and i in unescaped_characters:
                name = ""
                while i < len(user_input) and user_input[i] not in ['\'', '\"', ' ']:
                    name += user_input[i]
                    i += 1
                result += self.variables.get(name, '')
            i += 1

        return result

from src.parser.preprocessor import Preprocessor


class SplitterIntoCommands(object):

    def split_into_commands(self, data):
        return self._split_each_command_into_words(self._split_with_characters_not_in_quotes(data, '|'))

    def _split_each_command_into_words(self, commands):
        result = []
        for command in commands:
            words = self._split_with_characters_not_in_quotes(command, ' ')
            words = list(filter(lambda x: x != '', words))
            result.append(words)

        return result

    @staticmethod
    def _split_with_characters_not_in_quotes(data, character):
        indices = Preprocessor.find_symbols_not_in_quotes(data, character)
        pairs = list(zip([0] + list(map(lambda x: x + 1, indices)), indices + [len(data)]))
        return [data[l:r] for (l, r) in pairs]

from src.parser.parsing_utils import find_symbols_not_in_quotes


class SplitterIntoCommands(object):
    PIPE = '|'
    SPLITTETS = [' ', '\t', '\n']

    @classmethod
    def split_into_commands(cls, data):
        return cls._split_each_command_into_words(cls._split_with_characters_not_in_quotes(data, cls.PIPE))

    @classmethod
    def _split_each_command_into_words(cls, commands):
        result = []
        for command in commands:
            words = cls._split_with_characters_not_in_quotes(command, cls.SPLITTETS)
            words = list(filter(lambda x: x != '', words))
            result.append(words)

        return result

    @classmethod
    def _split_with_characters_not_in_quotes(cls, data, characters):
        indices = find_symbols_not_in_quotes(data, characters)
        pairs = list(zip([0] + list(map(lambda x: x + 1, indices)), indices + [len(data)]))
        return [data[l:r] for (l, r) in pairs]

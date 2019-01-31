from src.parser.parsing_utils import check_quotes_correctness


class Reader(object):
    """
    Class for reading user's input.
    """
    @classmethod
    def read(cls):
        """
        Read lines until it's number of opened quotes is equal to the number of closing using bash rules.
        :return: user's input
        """
        result = input()
        while not check_quotes_correctness(result) or result.strip().endswith('|'):
            result += '\n'
            result += input()
        return result

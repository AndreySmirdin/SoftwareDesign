from src.parser.parsing_utils import check_quotes_correctness


class Reader(object):

    @classmethod
    def read(cls):
        result = input()
        while not check_quotes_correctness(result):
            result += '\n'
            result += input()
        return result

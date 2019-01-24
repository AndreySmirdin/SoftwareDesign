class Reader(object):

    @classmethod
    def read(cls):
        result = input()
        while cls.expect_another_line(result):
            result += '\n'
            result += input()
        return result

    @classmethod
    def expect_another_line(cls, result):
        if result.count('\'') % 2 != 0 or result.count('\"') % 2 != 0:
            return True
        return False

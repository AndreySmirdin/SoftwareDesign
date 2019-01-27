from src.executor import Executor
from src.parser.parser import Parser
from src.reader import Reader


class Interpreter(object):
    """
    Simple bash-like interpreter. It supports such commands as:
    -   cat <FILE>
    -   pwd
    -   wc <FILE>
    -   echo <arg1> <arg2> ...
    Also it supports creating variables in a format `name=value`.
    Supports strong and weak quoting. Doesn't support escaping of symbols.
    """
    def __init__(self):
        variables = {}
        self.parser = Parser(variables)
        self.executor = Executor(variables)

    def run(self):
        """
        Running interpreter. It is will execute commands until it meets `exit`.
        """
        while True:
            user_input = Reader.read()
            commands = self.parser.parse(user_input)
            try:
                should_continue, result = self.executor.execute(commands)
                if result:
                    print(result)
                if not should_continue:
                    break
            except Exception as e:
                print(e)


if __name__ == "__main__":
    Interpreter().run()

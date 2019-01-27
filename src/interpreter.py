from src.executor import Executor
from src.parser.parser import Parser
from src.reader import Reader


class Interpreter(object):

    def __init__(self):
        variables = {}
        self.parser = Parser(variables)
        self.executor = Executor(variables)

    def run(self):
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

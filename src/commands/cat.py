from src.commands.abstract_command import AbstractCommand


class Cat(AbstractCommand):
    name = 'cat'

    @classmethod
    def run(cls, args, stdin):
        file_name = args[0] if args else stdin
        with open(file_name, 'r') as file:
            return file.readlines()

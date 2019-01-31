from abc import ABC, abstractmethod


class AbstractCommand(ABC):
    """
    Basic class for all commands that are supported by interpreter.
    """
    @classmethod
    @abstractmethod
    def name(cls):
        """
        Property-like function to get command name.
        :rtype: command name
        """
        pass

    @classmethod
    @abstractmethod
    def run(cls, args, stdin):
        """
        Executing the command.
        :param args: command arguments
        :param stdin: standard input
        """
        pass

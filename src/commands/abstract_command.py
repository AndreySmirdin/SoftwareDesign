from abc import ABC, abstractmethod


class AbstractCommand(ABC):

    @classmethod
    @abstractmethod
    def name(cls):
        pass

    @classmethod
    @abstractmethod
    def run(cls, args, stdin):
        pass

    # @classmethod
    # def open_if_exists(cls, file):

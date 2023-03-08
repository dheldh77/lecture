from abc import ABCMeta, abstractmethod


class Equipment(metaclass=ABCMeta):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def analyze(self):
        pass

    @abstractmethod
    def report(self):
        pass

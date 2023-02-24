import random
from abc import ABCMeta, abstractmethod


class IState(metaclass=ABCMeta):
    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self, seed=random.random()):
        pass

    @abstractmethod
    def dispense(self):
        pass

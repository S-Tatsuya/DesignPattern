from abc import abstractmethod
from .Beverage import Beverage


class CondimentDecorator(Beverage):
    @property
    @abstractmethod
    def Description(self):
        pass

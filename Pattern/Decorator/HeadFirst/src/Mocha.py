from .CondimentDecorator import CondimentDecorator
from .Beverage import Beverage


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @property
    def Description(self):
        return self._beverage.Description + ", モカ"

    def cost(self):
        return 0.20 + self._beverage.cost()

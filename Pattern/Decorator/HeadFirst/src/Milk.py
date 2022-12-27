from .CondimentDecorator import CondimentDecorator
from .Beverage import Beverage


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @property
    def Description(self):
        return self._beverage.Description + ", スムースミルク"

    def cost(self):
        return 0.10 + self._beverage.cost()

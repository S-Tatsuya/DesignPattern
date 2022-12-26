from .CondimentDecorator import CondimentDecorator
from .Beverage import Beverage


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @property
    def Description(self):
        return self._beverage.Description + ", 豆乳"

    def cost(self):
        return 0.15 + self._beverage.cost()

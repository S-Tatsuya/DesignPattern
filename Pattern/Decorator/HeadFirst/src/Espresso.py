from .Beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        self._description = "エスプレッソ"

    def cost(self):
        return 1.99

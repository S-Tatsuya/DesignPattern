from .Beverage import Beverage


class Decaf(Beverage):
    def __init__(self):
        self._description = "カフェイン抜き"

    def cost(self):
        return 1.05

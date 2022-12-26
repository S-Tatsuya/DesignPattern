from .Beverage import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        self._description = "ダークロースト"

    def cost(self):
        return 0.99

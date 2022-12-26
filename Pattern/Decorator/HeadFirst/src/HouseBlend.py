from .Beverage import Beverage


class HouseBlend(Beverage):
    def __init__(self):
        self._description = "ハウスブレンドコーヒー"

    def cost(self):
        return 0.89

from src.framework.Product import Product
import copy


class UnderlinePen(Product):
    def __init__(self, ulchar):
        self._ulchar = ulchar

    def use(self, s):
        length = len(s)
        print("")
        print(f'"{s}"')
        print(" ", end="")
        for _ in range(0, length):
            print(self._ulchar, end="")
        print("")

    def createClone(self):
        return copy.deepcopy(self)

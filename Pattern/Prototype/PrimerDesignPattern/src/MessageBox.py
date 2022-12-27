from src.framework.Product import Product
import copy


class MessageBox(Product):
    def __init__(self, char):
        self._decochar = char

    def use(self, s):
        length = len(s)

        for _ in range(0, length + 4):
            print(self._decochar, end="")
        print("")

        print(f"{self._decochar} {s} {self._decochar}")

        for _ in range(0, length + 4):
            print(self._decochar, end="")
        print("")

    def createClone(self):
        return copy.deepcopy(self)

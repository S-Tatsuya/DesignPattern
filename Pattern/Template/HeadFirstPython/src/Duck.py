class Duck:
    def __init__(self, name, wight):
        self._name = name
        self._wight = wight

    @property
    def name(self):
        return self._name

    @property
    def wight(self):
        return self._wight

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.wight == other.wight

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplementedError()

        return self.wight < other.wight

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__lt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

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

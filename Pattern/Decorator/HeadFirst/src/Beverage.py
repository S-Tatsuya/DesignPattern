from abc import ABCMeta, abstractmethod


class Beverage(metaclass=ABCMeta):
    _description = "不明な飲み物"

    @property
    def Description(self):
        return self._description

    @abstractmethod
    def cost(self) -> float:
        pass

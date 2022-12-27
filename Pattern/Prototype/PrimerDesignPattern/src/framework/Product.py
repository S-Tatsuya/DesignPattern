from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self, s):
        pass

    @abstractmethod
    def createClone(self) -> Product:
        pass

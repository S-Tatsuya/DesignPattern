from abc import ABCMeta, abstractmethod


class IDisplayElement(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        raise NotImplementedError()

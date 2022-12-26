from abc import ABCMeta, abstractmethod


class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def update(self, temp, humidity, pressure):
        raise NotImplementedError()

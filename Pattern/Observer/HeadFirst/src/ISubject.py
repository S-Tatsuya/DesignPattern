from abc import ABCMeta, abstractmethod
from .IObserver import IObserver


class ISubject(metaclass=ABCMeta):
    @abstractmethod
    def register_observer(self, obj: IObserver):
        raise NotImplementedError()

    @abstractmethod
    def remove_observer(self, obj: IObserver):
        raise NotImplementedError()

    @abstractmethod
    def notify_observer():
        raise NotImplementedError()

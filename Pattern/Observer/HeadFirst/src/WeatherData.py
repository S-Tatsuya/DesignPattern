from .ISubject import ISubject
from .IObserver import IObserver


class WeatherData(ISubject):
    def __init__(self):
        self._observers = []
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    def register_observer(self, obj: IObserver):
        if obj not in self._observers:
            self._observers.append(obj)

    def remove_observer(self, obj: IObserver):
        if obj in self._observers:
            self._observers.remove(obj)

    def notify_observer(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def mesurements_changed(self):
        self.notify_observer()

    def set_mesurements(self, temp, humi, pres):
        self._temperature = temp
        self._humidity = humi
        self._pressure = pres
        self.mesurements_changed()

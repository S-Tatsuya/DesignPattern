from .IObserver import IObserver
from .ISubject import ISubject
from .IDisplayElement import IDisplayElement


class CurrentConditionsDisplay(IObserver, IDisplayElement):
    def __init__(self, weather_data: ISubject):
        self._weather_data = weather_data
        self._weather_data.register_observer(self)
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    def update(self, temp, humidity, pressure):
        self._temperature = temp
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self):
        print(f"現在の気象状況:温度{self._temperature}度 湿度{self._humidity}%")

from .IObserver import IObserver
from .ISubject import ISubject
from .IDisplayElement import IDisplayElement


class StatisticsDisplay(IObserver, IDisplayElement):
    def __init__(self, weather_data: ISubject):
        self._weather_data = weather_data
        self._weather_data.register_observer(self)
        self._average = 0
        self._max = 0
        self._min = 999
        self._temp_logs = []

    def update(self, temp, humidity, pressure):
        _ = humidity
        _ = pressure
        self._average = self.__average(temp)
        self._max = max(self._max, temp)
        self._min = min(self._min, temp)
        self.display()

    def __average(self, temp):
        self._temp_logs.append(temp)
        return sum(self._temp_logs) / len(self._temp_logs)

    def display(self):
        print(f"平均/最高/最低気温: {self._average}/{self._max}/{self._min}")

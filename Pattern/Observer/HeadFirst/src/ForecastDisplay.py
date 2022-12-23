from .IObserver import IObserver
from .ISubject import ISubject
from .IDisplayElement import IDisplayElement


class ForecastDisplay(IObserver, IDisplayElement):
    def __init__(self, weather_data: ISubject):
        self._weather_data = weather_data
        self._weather_data.register_observer(self)
        self._display_message = ["天候は良くなります！", "より寒く雨模様の天候に注意してください", "ほとんど同じです"]
        self._counter = 0

    def update(self, temp, humidity, pressure):
        _ = humidity
        _ = pressure
        _ = temp
        self.display()

    def display(self):
        print(f"予報: {self._display_message[self._counter]}")
        if self._counter > 2:
            self._counter = 0
        else:
            self._counter += 1

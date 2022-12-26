from src.WeatherData import WeatherData
from src.CurrentConditionsDisplay import CurrentConditionsDisplay
from src.StatisticsDisplay import StatisticsDisplay
from src.ForecastDisplay import ForecastDisplay


def test_weather_data():
    weather_data = WeatherData()

    currentDisplay = CurrentConditionsDisplay(weather_data)
    statistics_display = StatisticsDisplay(weather_data)
    forcast_display = ForecastDisplay(weather_data)

    _ = currentDisplay
    _ = statistics_display
    _ = forcast_display

    weather_data.set_mesurements(27, 65, 30.4)
    weather_data.set_mesurements(28, 70, 29.2)
    weather_data.set_mesurements(26, 90, 29.2)

    assert True

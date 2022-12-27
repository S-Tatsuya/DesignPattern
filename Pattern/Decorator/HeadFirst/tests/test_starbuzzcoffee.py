from src.Espresso import Espresso
from src.DarkRoast import DarkRoast
from src.HouseBlend import HouseBlend
from src.Mocha import Mocha
from src.Whip import Whip
from src.Soy import Soy


def test_starbuzzcoffee():
    beverage = Espresso()
    print(f"{beverage.Description} $ {beverage.cost()}")

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.Description} $ {beverage2.cost()}")

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.Description} $ {beverage3.cost()}")
    assert True

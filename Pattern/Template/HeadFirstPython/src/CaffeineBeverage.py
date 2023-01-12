from abc import ABCMeta, abstractmethod
from typing import final


class CaffeineBeverage(metaclass=ABCMeta):
    def prepare_recipe(self):
        print(self.boil_water())
        print(self.brew())
        print(self.pour_in_cup())
        print(self.add_condiments())

    @final
    def boil_water(self):
        return "お湯を沸かします"

    @abstractmethod
    def brew(self):
        pass

    @final
    def pour_in_cup(self):
        return "カップに注ぎます"

    @abstractmethod
    def add_condiments(self):
        pass

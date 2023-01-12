from abc import ABCMeta, abstractmethod


class CaffeineBeverage(metaclass=ABCMeta):
    @abstractmethod
    def prepare_recipe(self):
        pass

    def boil_water(self):
        return "お湯を沸かします"

    def pour_in_cup(self):
        return "カップに注ぎます"

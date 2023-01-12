from src.CaffeineBeverage import CaffeineBeverage


class Coffee(CaffeineBeverage):
    def prepare_recipe(self):
        print(self.boil_water())
        print(self.brew_coffee_grinds())
        print(self.pour_in_cup())
        print(self.add_sugar_and_milk())

    def brew_coffee_grinds(self):
        return "フィルタでコーヒーをドリップします"

    def add_sugar_and_milk(self):
        return "砂糖とミルクを追加します"

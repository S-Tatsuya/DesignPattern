from src.CaffeineBeverage import CaffeineBeverage


class Tea(CaffeineBeverage):
    def prepare_recipe(self):
        print(self.boil_water())
        print(self.steep_tea_bag())
        print(self.pour_in_cup())
        print(self.add_lemon())

    def steep_tea_bag(self):
        return "紅茶を浸します"

    def add_lemon(self):
        return "レモンを追加します"

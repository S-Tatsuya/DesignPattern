class Coffee:
    def prepare_recipe(self):
        print(self.boil_water())
        print(self.brew_coffee_grinds())
        print(self.pour_in_cup())
        print(self.add_sugar_and_milk())

    def boil_water(self):
        return "お湯を沸かします"

    def brew_coffee_grinds(self):
        return "フィルタでコーヒーをドリップします"

    def pour_in_cup(self):
        return "カップに注ぎます"

    def add_sugar_and_milk(self):
        return "砂糖とミルクを追加します"

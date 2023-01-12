class Tea:
    def prepare_recipe(self):
        print(self.boil_water())
        print(self.steep_tea_bag())
        print(self.add_lemon())
        print(self.pour_in_cup())

    def boil_water(self):
        return "お湯を沸かします"

    def steep_tea_bag(self):
        return "紅茶を浸します"

    def add_lemon(self):
        return "レモンを追加します"

    def pour_in_cup(self):
        return "カップに注ぎます"

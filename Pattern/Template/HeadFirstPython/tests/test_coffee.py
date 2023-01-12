from src.Coffee import Coffee


class TestCoffee:
    def test_coffee_boil_water(self):
        sut = Coffee()

        assert sut.boil_water() == "お湯を沸かします"

    def test_coffee_brew_coffee_grinds(self):
        sut = Coffee()

        assert sut.brew_coffee_grinds() == "フィルタでコーヒーをドリップします"

    def test_coffee_pour_in_cup(self):
        sut = Coffee()

        assert sut.pour_in_cup() == "カップに注ぎます"

    def test_coffee_add_sugar_and_milk(self):
        sut = Coffee()

        assert sut.add_sugar_and_milk() == "砂糖とミルクを追加します"

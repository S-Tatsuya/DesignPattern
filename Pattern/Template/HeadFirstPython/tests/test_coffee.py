import io
import pytest

from src.Coffee import Coffee


class TestCoffee:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.sut = Coffee()

    def test_prepare_recipe_add_condiments(self, capfd, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("y\n"))
        self.sut.prepare_recipe()

        out, err = capfd.readouterr()
        assert out == (
            "お湯を沸かします\n"
            "フィルタでコーヒーをドリップします\n"
            "カップに注ぎます\n"
            "コーヒーに砂糖とミルクをいれますか？(y/n)\n"
            "砂糖とミルクを追加します\n"
        )

        assert err == ""

    def test_prepare_recipe_not_condiments(self, capfd, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("n\n"))
        self.sut.prepare_recipe()

        out, err = capfd.readouterr()
        assert out == (
            "お湯を沸かします\n" "フィルタでコーヒーをドリップします\n" "カップに注ぎます\n" "コーヒーに砂糖とミルクをいれますか？(y/n)\n"
        )
        assert err == ""

    def test_coffee_boil_water(self):
        assert self.sut.boil_water() == "お湯を沸かします"

    def test_coffee_brew_coffee_grinds(self):
        assert self.sut.brew() == "フィルタでコーヒーをドリップします"

    def test_coffee_pour_in_cup(self):
        assert self.sut.pour_in_cup() == "カップに注ぎます"

    def test_coffee_add_sugar_and_milk(self):
        assert self.sut.add_condiments() == "砂糖とミルクを追加します"

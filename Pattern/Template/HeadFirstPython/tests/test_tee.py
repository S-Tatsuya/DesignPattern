import pytest

from src.Tea import Tea


class TestTea:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.sut = Tea()

    def test_prepare_recipe(self, capfd):
        self.sut.prepare_recipe()

        out, err = capfd.readouterr()
        assert out == "お湯を沸かします\n紅茶を浸します\nレモンを追加します\nカップに注ぎます\n"
        assert err == ""

    def test_tee_boil_water(self):
        assert self.sut.boil_water() == "お湯を沸かします"

    def test_tee_steep_tea_bag(self):
        assert self.sut.steep_tea_bag() == "紅茶を浸します"

    def test_tee_add_lemon(self):
        assert self.sut.add_lemon() == "レモンを追加します"

    def test_tee_pour_in_cup(self):
        assert self.sut.pour_in_cup() == "カップに注ぎます"

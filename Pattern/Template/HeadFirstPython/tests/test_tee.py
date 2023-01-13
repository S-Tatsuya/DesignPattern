import io
import pytest

from src.Tea import Tea


class TestTea:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.sut = Tea()

    def test_prepare_recipe_add_condiments(self, capfd, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("y\n"))
        self.sut.prepare_recipe()

        out, err = capfd.readouterr()
        assert out == (
            "お湯を沸かします\n" "紅茶を浸します\n" "カップに注ぎます\n" "紅茶にレモンをいれますか?(y/n)\n" "レモンを追加します\n"
        )
        assert err == ""

    def test_prepare_recipe_not_condiments(self, capfd, monkeypatch):
        monkeypatch.setattr("sys.stdin", io.StringIO("n\n"))
        self.sut.prepare_recipe()

        out, err = capfd.readouterr()
        assert out == ("お湯を沸かします\n" "紅茶を浸します\n" "カップに注ぎます\n" "紅茶にレモンをいれますか?(y/n)\n")
        assert err == ""

    def test_tee_boil_water(self):
        assert self.sut.boil_water() == "お湯を沸かします"

    def test_tee_steep_tea_bag(self):
        assert self.sut.brew() == "紅茶を浸します"

    def test_tee_add_lemon(self):
        assert self.sut.add_condiments() == "レモンを追加します"

    def test_tee_pour_in_cup(self):
        assert self.sut.pour_in_cup() == "カップに注ぎます"

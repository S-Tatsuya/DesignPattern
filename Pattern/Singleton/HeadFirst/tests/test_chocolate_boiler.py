import pytest

from src.ChocolateBoiler import ChocolateBoiler


class TestChocolateBoiler:
    @pytest.fixture(autouse=True)
    def setup_chocolateBoiler(self):
        self.sut = ChocolateBoiler.get_instance()
        self.sut.clean()

    def test_is_empty(self):
        assert self.sut.is_empty is True

    def test_is__boiled(self):
        assert self.sut.is_boiled is False

    def test_fill(self):
        assert self.sut.is_empty is True
        assert self.sut.is_boiled is False

        self.sut.fill()
        assert self.sut.is_empty is False
        assert self.sut.is_boiled is False

    def test_boil(self):
        self.sut.boil()
        assert self.sut.is_empty is True
        assert self.sut.is_boiled is False

        self.sut.fill()
        assert self.sut.is_empty is False
        assert self.sut.is_boiled is False

        self.sut.boil()
        assert self.sut.is_empty is False
        assert self.sut.is_boiled is True

    def test_drain(self):
        self.sut.drain()
        assert self.sut.is_empty is True
        assert self.sut.is_boiled is False

        self.sut.fill()
        self.sut.drain()
        assert self.sut.is_empty is False
        assert self.sut.is_boiled is False

        self.sut.boil()
        self.sut.drain()
        assert self.sut.is_empty is True
        assert self.sut.is_boiled is True

    def test_singleton(self):
        result = ChocolateBoiler.get_instance()
        assert self.sut is result

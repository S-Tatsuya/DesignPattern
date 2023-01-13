from src.Duck import Duck


class TestDuck:
    def test_duck_wight(self):
        sut = Duck("duck1", 1)

        assert sut.wight == 1
        assert sut.name == "duck1"

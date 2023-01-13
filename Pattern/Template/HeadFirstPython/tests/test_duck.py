from src.Duck import Duck


class TestDuck:
    def test_wight_and_name(self):
        sut = Duck("duck1", 1)

        assert sut.wight == 1
        assert sut.name == "duck1"

    def test_compare(self):
        sut_large = Duck("duck_large", 5)
        sut_large2 = Duck("duck_large2", 5)
        sut_small = Duck("duck_small", 1)

        assert sut_large > sut_small
        assert sut_small < sut_large
        assert sut_large == sut_large2
        assert sut_large != sut_small
        assert sut_large >= sut_small
        assert sut_small <= sut_large

    def test_duck_sort(self):
        suts = [
            Duck("duck5", 5),
            Duck("duck1", 1),
            Duck("duck7", 7),
            Duck("duck4", 4),
            Duck("duck2", 2),
            Duck("duck5", 5),
        ]

        result = sorted(suts)

        assert result == [
            Duck("duck1", 1),
            Duck("duck2", 2),
            Duck("duck4", 4),
            Duck("duck5", 5),
            Duck("duck5", 5),
            Duck("duck7", 7),
        ]

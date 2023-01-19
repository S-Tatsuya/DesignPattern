import pytest

from src.Singleton import Singleton


class TestSingleton:
    def test_constructor(self):
        sut = Singleton.get_instance()
        result = Singleton.get_instance()
        assert sut is not None
        assert result is not None
        assert sut is result

    def test_singleton_constructor(self):
        with pytest.raises(NotImplementedError) as e:
            _ = Singleton()

        assert str(e.value) == ""

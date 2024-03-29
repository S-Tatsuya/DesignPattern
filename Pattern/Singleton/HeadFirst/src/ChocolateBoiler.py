class ChocolateBoiler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._is_empty = True
        self._is_boiled = False

    def fill(self):
        if self._is_empty:
            self._is_empty = False
            self._is_boiled = False

    def boil(self):
        if self.is_empty:
            return
        if self.is_boiled:
            return

        self._is_boiled = True

    def drain(self):
        if self.is_empty:
            return
        if not self.is_boiled:
            return

        self._is_empty = True

    def clean(self):
        self._is_empty = True
        self._is_boiled = False

    @property
    def is_empty(self):
        return self._is_empty

    @property
    def is_boiled(self):
        return self._is_boiled

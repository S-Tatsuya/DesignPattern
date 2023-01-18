class Singleton:
    def __init__(self):
        raise NotImplementedError()

    unique_instance = None

    @classmethod
    def get_instance(cls):
        if cls.unique_instance is None:
            cls.unique_instance = cls.__new__(cls)
        return cls.unique_instance

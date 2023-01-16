class Singleton:
    unique_instance = None

    @classmethod
    def get_instance(cls):
        if cls.unique_instance is None:
            cls.unique_instance = Singleton()
        return cls.unique_instance

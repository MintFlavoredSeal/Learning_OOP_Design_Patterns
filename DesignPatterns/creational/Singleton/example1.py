class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    

class SomeSingleton(metaclass=SingletonMeta):
    def some_behavior(self):
        print(f"you can define it's own methods : {self}")


if __name__ == "__main__":
    # The client code.

    s1 = SomeSingleton()
    s2 = SomeSingleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
        s1.some_behavior()
        s2.some_behavior()
    else:
        print("Singleton failed, variables contain different instances.")
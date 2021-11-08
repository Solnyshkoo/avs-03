from abc import ABC


class Vehicle(ABC):
    """
    Abstract class -- every vehicle must inherit it!
    No default constructor provided
    """
    def __str__(self) -> str:
        pass

    def distance(self) -> float:
        """
        Calculates distance which vehicle is able to travel with full tank.
        :return:
        """
        pass

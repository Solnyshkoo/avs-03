from Vehicle import Vehicle
from random import randint, random


class Truck(Vehicle):
    def __init__(self,
                 randomly=False,
                 capacity=None,
                 consumption=None,
                 lifting=None,
                 logger=None):
        """
        Creates a truck with given parameters (or random if randomly is True)

        :param randomly: bool, Set True if you want your figure to be created randomly
        :param capacity: int
        :param consumption: float
        :param lifting: int
        :param logger:
        """
        # Check if we need to randomly create parameters
        if randomly:
            self.capacity = randint(30, 70)
            self.consumption = 2 + abs(random()) * 10
            self.lifting = randint(2000, 5000)
        else:
            # Check if input data is incorrect
            if (capacity is None or consumption is None or lifting is None) and logger:
                logger.error("Randomly has been set to False and no arguments were provided!\n")
            self.capacity = capacity
            self.consumption = consumption
            self.lifting = lifting

        # Here goes logging stuff
        if logger:
            self.logger = logger

            if randomly:
                self.logger.info("Successfully created truck with random parameters:"
                                 f"capacity={self.capacity}, consumption={self.consumption}, lifting={self.lifting}")
            else:
                self.logger.info("Successfully created truck with given parameters:"
                                 f"capacity={capacity}, consumption={consumption}, lifting={lifting}")

    def distance(self) -> float:
        return (self.capacity / self.consumption) * 100

    def __str__(self) -> str:
        return f"It is Truck: Fuel capacity = {self.capacity} (litres)," \
               f"Fuel consumption = {self.consumption} (litres/100km)" \
               f"Lifting = {self.lifting} (kg)" \
               f"Maximum distance = {self.distance()} (km)"


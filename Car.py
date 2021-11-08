from Vehicle import Vehicle
from random import randint, random


class Car(Vehicle):
    def __init__(self,
                 randomly=False,
                 capacity=None,
                 consumption=None,
                 max_speed=None,
                 logger=None):
        """
        Creates a car with given parameters (or random if randomly is True)

        :param randomly: bool, Set True if you want your figure to be created randomly
        :param capacity: int
        :param consumption: float
        :param max_speed: int
        :param logger:
        """

        # Check if we need to randomly create parameters
        if randomly:
            self.capacity = randint(30, 70)
            self.consumption = 2 + abs(random()) * 10
            self.max_speed = randint(70, 220)
        else:
            # Check if input data is incorrect
            if (capacity is None or consumption is None or max_speed is None) and logger:
                logger.error("Randomly has been set to False and no arguments were provided!\n")
            self.capacity = capacity
            self.consumption = consumption
            self.max_speed = max_speed

        # Here goes logging stuff
        if logger:
            self.logger = logger

            if randomly:
                logger.info("Successfully created car with random parameters:"
                            f"capacity={self.capacity}, consumption={self.consumption}, max_speed={self.max_speed}")
            else:
                logger.info("Successfully created car with given parameters:"
                            f"capacity={capacity}, consumption={consumption}, max_speed={max_speed}")
        else:
            self.logger = None

    def distance(self) -> float:
        return (self.capacity / self.consumption) * 100

    def __str__(self) -> str:
        return f"It is Car: Fuel capacity = {self.capacity} (litres)," \
               f"Fuel consumption = {self.consumption} (litres/100km)" \
               f"Maximum speed = {self.max_speed} (km)" \
               f"Maximum distance = {self.distance()} (km)"


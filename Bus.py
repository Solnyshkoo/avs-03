from Vehicle import Vehicle
from random import randint, random


class Bus(Vehicle):
    def __init__(self,
                 randomly=False,
                 capacity=None,
                 consumption=None,
                 person_capacity=None,
                 logger=None):
        """
        Creates a bus with given parameters (or random if randomly is True)

        :param randomly: bool, Set True if you want your figure to be created randomly
        :param capacity: int
        :param consumption: float
        :param person_capacity: int
        :param logger:
        """
        # Check if we need to randomly create parameters
        if randomly:
            self.capacity = randint(30, 70)
            self.consumption = 2 + abs(random()) * 10
            self.person_capacity = randint(2000, 5000)
        else:
            # Check if input data is incorrect
            if (capacity is None or consumption is None or person_capacity is None) and logger:
                logger.error("Randomly has been set to False and no arguments were provided!\n")

            self.capacity = capacity
            self.consumption = consumption
            self.person_capacity = person_capacity

        # Here goes logging stuff
        if logger:
            self.logger = logger

            if randomly:
                logger.info("Successfully created bus with random parameters:"
                            f"capacity={self.capacity}, consumption={self.consumption}, "
                            f"person capacity={self.person_capacity}")
            else:
                logger.info("Successfully created bus with given parameters:"
                            f"capacity={capacity}, consumption={consumption}, person capacity={person_capacity}")
        else:
            self.logger = None

    def distance(self) -> float:
        return (self.capacity / self.consumption) * 100

    def __str__(self) -> str:
        return f"It is Bus: Fuel capacity = {self.capacity} (litres)," \
               f"Fuel consumption = {self.consumption} (litres/100km)" \
               f"Person capacity = {self.person_capacity} (kg)" \
               f"Maximum distance = {self.distance()} (km)"


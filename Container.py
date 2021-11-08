from typing import NoReturn

from random import randint

from Car import Car
from Truck import Truck
from Bus import Bus


class ContainerOverflow(Exception):
    pass


class Container:
    def __init__(self, randomly=False, amount=None, filename=None, logger=None):
        """
        Constructor of container.
        No more than 10000 elements can be kept!

        :param randomly: bool set True if you want random contents
        :param amount: int is randomly=True, amount of elements that to generate
        :param filename: if given, opens and takes info from it
        :param logger:
        """

        self.container = []
        self.logger = logger

        if randomly:
            if amount > 10000:
                if logger:
                    logger.critical("No more than 10000 elements are allowed! Raising exception")
                raise ContainerOverflow("No more than 10000 elements are allowed!")
            self._random_inputs_(amount)

        if logger:
            logger.info("Created container")

        if filename:
            if logger:
                logger.info(f"Reading from {filename} file")
            self._read_from_file_(filename)

    def _read_from_file_(self, filename: str) -> None:
        """
        Private method for initialisation from file.
        File must be in .txt format.
        :param filename:
        :return:
        """
        with open(filename, 'r') as file:
            input_string = file.read()
            data = list(map(int, input_string.split()))

            for i in range(0, len(data), 4):
                if data[i] == 1:
                    self.container.append(Car(capacity=data[i + 1],
                                              consumption=data[i + 2],
                                              max_speed=data[i + 3],
                                              logger=self.logger))
                elif data[i] == 2:
                    self.container.append(Bus(capacity=data[i + 1],
                                              consumption=data[i + 2],
                                              person_capacity=data[i + 3],
                                              logger=self.logger))
                elif data[i] == 3:
                    self.container.append(Truck(capacity=data[i + 1],
                                                consumption=data[i + 2],
                                                lifting=data[i + 3],
                                                logger=self.logger))

                else:
                    if self.logger:
                        self.logger.error(f"Unknown type of vehicle {data[i]}. Skipping")

        if len(self.container) > 10000:
            if self.logger:
                self.logger.critical("No more than 10000 elements are allowed! Raising exception")
            raise ContainerOverflow("No more than 10000 elements are allowed!")

        if self.logger:
            self.logger.info(f"Successfully read {len(data)} vehicles from {filename}")

    def _random_inputs_(self, amount) -> NoReturn:
        """
        Fills container with random vehicles
        :param amount: int, amount of vehicles to be generated
        :return:
        """
        if self.logger:
            self.logger.info("Starting random filling")

        for i in range(amount):
            k = randint(1, 3)
            if k == 1:
                self.container.append(Car(randomly=True, logger=self.logger))
            elif k == 2:
                self.container.append(Bus(randomly=True, logger=self.logger))
            elif k == 3:
                self.container.append(Truck(randomly=True, logger=self.logger))

        if self.logger:
            self.logger.info(f"Filled container with {amount} random vehicles")

    def __str__(self) -> str:
        r_str = f"Container contains {len(self.container)} elements:\n" \
                f"--------------------------------------------------\n"

        for i in range(len(self.container)):
            r_str += f"{i}. {self.container[i]}\n" \
                     f"--------------------------------------------------\n"

        return r_str

    def to_file(self, filename: str) -> NoReturn:
        """
        More practical way to read get data other than __str__ method.

        :param filename: output file
        :return:
        """
        if self.logger:
            self.logger.info(f'Opening {filename} to write contains of container to it')

        with open(filename, 'w') as file:
            file.write(f"Container contains {len(self.container)} elements:\n"
                       f"--------------------------------------------------\n")

            for i in range(len(self.container)):
                file.write(f"{i}. {self.container[i]}\n"
                           f"--------------------------------------------------\n")

        if self.logger:
            self.logger.info(f'Written {len(self.container)} vehicles to {filename}. '
                             f'File closed')

    def shaker_sort(self):
        is_sorted = False
        start = 0
        end = len(self.container) - 1
        counter = 0

        while not is_sorted:
            is_sorted = True
            for i in range(start, end):
                counter += 1
                if self.container[i].distance() > self.container[i + 1].distance():
                    self.container[i], self.container[i + 1] = self.container[i + 1], self.container[i]
                    is_sorted = False

            if is_sorted:
                break

            end -= 1
            is_sorted = True

            for i in range(end - 1, start - 1, -1):
                counter += 1
                if self.container[i + 1].distance() < self.container[i].distance():
                    self.container[i], self.container[i + 1] = self.container[i + 1], self.container[i]
                    is_sorted = False

            start += 1

import abc

class Transportation(abc.ABC):
    def __init__(self, start_place, end_place, distance):
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance

    @abc.abstractmethod   
    def find_cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

        # self.start_place = start_place
        # self.end_place = end_place
        # self.distance = distance

    def find_cost(self):
        self.total = 0
        return self.total

class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance

    def find_cost(self):
        self.total = 40 * self.distance
        return self.total

class Train(Transportation):
    def __init__(self, start_place, end_place, distance, station):
        super().__init__(start_place, end_place, distance)

        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance
        self.station = station

    def find_cost(self):
        self.total = 5 * self.station
        return self.total


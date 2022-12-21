import abc

class StationaryGood(abc.ABC):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    
    def getCost(self):
        pass

class Magazine(StationaryGood):
    def __init__(self, p, q):
        super().__init__(p, q)
        
    def getCost(self):
        self.cost = self.p * self.q
        return self.cost

class Book(StationaryGood):
    def __init__(self, p, q):
        super().__init__(p, q)
        
    def getCost(self):
        self.cost = (self.p * self.q) * 90 / 100
        return self.cost

class Ribbon(StationaryGood):
    def __init__(self, q, p=5):
        super().__init__(p, q)
        
    def getCost(self):
        self.cost = 5 * self.q
        return self.cost

magazine = Magazine(70, 3)
book = Book(200, 2)
ribbon = Ribbon(10)

basket = [magazine, book, ribbon]

def getTotalCost(basket):
    total = 0
    for i in basket:
        total += i.getCost()
    return total

print("Total cost is", getTotalCost(basket))

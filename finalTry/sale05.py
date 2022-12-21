import abc

class Sale_item(abc.ABC):
    def __init__(self, price, quantity, sale):
        self.price = price
        self.quantity = quantity
        self.sale = sale
        
    @abc.abstractmethod
    def get_cost(self):
        return (self.price * self.sale) * self.quantity
    
class Food(Sale_item, abc.ABC):
    def __init__(self, price, quantity, sale=1):
        super().__init__(price, quantity, sale)
    
    @abc.abstractmethod
    def get_cost(self):
        return super().get_cost()
   
class Book(Sale_item):
    def __init__(self, price, quantity, sale=0.85):
        super().__init__(price, quantity, sale)
        
    def get_cost(self):
        return super().get_cost()
    
class Appliance(Sale_item):
    def __init__(self, price, quantity, sale=1.07):
        super().__init__(price, quantity, sale)
        
    def get_cost(self):
        return super().get_cost()
    
class Itemized_food(Food):
    def __init__(self, price, quantity):
        super().__init__(price, quantity)
        
    def get_cost(self):
        return super().get_cost()
    
class Measured_food(Food):
    def __init__(self, price, quantity):
        super().__init__(price, quantity)
        
    def get_cost(self):
        return super().get_cost()
    
def get_total(basket):
    total = 0
    for i in basket:
        total += i.get_cost()
        
    return total


veg_oil = Itemized_food(40, 2)
mango = Measured_food(70, 1.8)
python = Book(200, 1)
rice_cooker = Appliance(1200, 1)

basket = [veg_oil, mango, python, rice_cooker]

print(get_total(basket))
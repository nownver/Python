from math import *

class QuadraticEquation():
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    
        # self._a = a
        # self._b = b
        # self._c = c

        # if self._a >= 0:
        #     self.__a = a
        # else:
        #     return 0

        # if self._b >= 0:
        #     self.__b = b
        # else:
        #     return 0

        # if self._c >= 0:
        #     self.__c = c
        # else:
        #     return 0

    def get_a(self, a):
        if a >= 0:
            self.__a = a
            return self.__a
        else:
            return 0

    def get_a(self, b):
        if b >= 0:
            self.__b = b
            return self.__b
        else:
            return 0

    def get_c(self, c):
        if c >= 0:
            self.__c = c
            return self.__c
        else:
            return 0
    
    def getDiscriminant(self):
        self.discriminant = (self.__b ** 2) - 4 * self.__a * self.__c
        return self.discriminant
    
    def getRoot1(self):
        if self.discriminant >= 0:
            # getDiscriminant()
            self.root1 = (- self.__b + (sqrt(self.discriminant))) / (2 * self.__a)
            return self.root1
        else:
            return 0

    def getRoot2(self):
        if self.discriminant >= 0:
            self.root2 = (- self.__b - (sqrt(self.discriminant))) / (2 * self.__a) 
            return self.root2
        else:
            return 0


q1 = QuadraticEquation(10,1,3)
# q1.get_a(2)
print(q1.getDiscriminant())
print(q1.getRoot2())
print(q1.getRoot1())


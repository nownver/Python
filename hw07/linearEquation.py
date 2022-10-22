class LinearEquation():
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d
    
    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f

    def isSolvable(self):
        if not (self.__a * self.__d) - (self.__b * self.__c) == 0:
            return True
        return False

    def getX(self):
        if self.isSolvable():
            answer = ((self.__e * self.__d) - (self.__b * self.__f)) / ((self.__a * self.__d) - (self.__b * self.__c))
            return answer
        else:
            return "denominator is 0"

    def getY(self):
        if self.isSolvable():
            answer = ((self.__a * self.__f) - (self.__e * self.__c)) / ((self.__a * self.__d) - (self.__b * self.__c))
            return answer
        else:
            return "denominator is 0"


sample1 = LinearEquation(1,1,12,3,9,7)
print(sample1.get_a())
print(sample1.isSolvable())
print(sample1.getX())
print(sample1.getY())

print("")

sample2 = LinearEquation(8,2,12,3,9,7)
print(sample2.get_b())
print(sample2.isSolvable())
print(sample2.getX())
print(sample2.getY())



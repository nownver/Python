import numpy as np
from numpy.polynomial import polynomial as P


class Poly:
    def __init__(self, x):
        self.x = list(x)
    
    # def print(self):
    #     np.polynomial.set_default_printstyle('unicode')
    #     t = np.polynomial.Polynomial(list(self.x))
    #     print(t)

    def print(self):
        for i in range(len(self.x)):
            if self.x == 0:
                continue
            else:
                print(f"{self.x[i]}", end ="")
                
    
    def add(self,t):
        new = t.x
        new.reverse()
        old = self.x
        old.reverse()
        older = np.poly1d(list(old))
        newest = np.poly1d(list(new))
        pls = np.polyadd(older, newest)
        pls = list(pls)
        pls.reverse()
        pls = np.polynomial.Polynomial(pls)
        return Poly(pls)
       
    def power(self,n):
        wow = P.polypow(self.x,n)
        q = np.polynomial.Polynomial(wow)
        return Poly(q)

    def scalar_multily(self,n):
        an_array = np.array(self.x)
        multiplied_array = an_array * n
        multiplied_array = np.polynomial.Polynomial(multiplied_array)
        return multiplied_array

    def multiply(self,p):
        new = list(p)
        new.reverse()
        old = list(self.x)
        old.reverse()
        oldest = np.poly1d(list(old))
        newer = np.poly1d(list(new))
        result = np.polymul(oldest, newer)
        result = list(result)
        result.reverse()
        result = np.polynomial.Polynomial(result)
        return result

    def diff(self):
        r = self.x
        r.reverse()
        deep = np.poly1d(list(r))
        derivative = deep.deriv()
        ag = list(derivative)
        ag.reverse()
        diff_re = np.polynomial.Polynomial(ag)
        return Poly(diff_re)
    
    def intergrate(self):
        inter = P.polyint(self.x)
        return Poly(inter)

    def eval(self,n):
        new = list(self.x)
        new.reverse()
        evalu = np.polyval(np.poly1d(list(new)),n)
        print(evalu)
        

ploy1 = Poly((1,0,-2))
ploy1.print()

q = ploy1.power(2)
q.print()

ploy1.print()

ploy1.eval(3)
r = ploy1.add(q)
r.diff().print()

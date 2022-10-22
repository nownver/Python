# ID: 63011335
# Name: Tawan Lekngam
# HWNo: 07
# QNo: 02

from __future__ import annotations


class Poly:
    def __init__(self, x: tuple):
        self.x = x

    def add(self, p: Poly) -> Poly:
        temp = [0] * max(self.size(), p.size()) 
        for i in range(self.size()):
            temp[i] += self.x[i]
        for j in range(p.size()):
            temp[j] += p.x[j]
        return Poly(tuple(temp))

    def scalar_multiply(self, n) -> Poly:
        temp = [i * n for i in self.x]
        return Poly(tuple(temp))

    def multiply(self, p: Poly) -> Poly:
        temp = [0] * (self.size() + p.size() - 1)
        for i in range(self.size()):
            for j in range(p.size()):
                temp[i + j] += self.x[i] * p.x[j]
        return Poly(tuple(temp))

    def power(self, n) -> Poly:
        res = Poly(self.x)
        for _ in range(n - 1):
            res = res.multiply(res)
        return res

    def diff(self) -> Poly:
        temp = [0] * (self.size() - 1)
        for i in range(self.size()):
            if i >= 1:
                temp[i - 1] = self.x[i] * i
        return Poly(tuple(temp))

    def integrate(self) -> Poly:
        temp = [0] * (self.size() + 1)
        for i in range(self.size()):
            temp[i + 1] = round(self.x[i] / (i + 1), 1)
        return Poly(tuple(temp))

    def eval(self, n):
        res = 0
        for i in range(self.size()):
            res += self.x[i] * pow(n, i)
        return res

    def print(self):
        res = ""
        for i in range(self.size()):
            if self.x[i] != 0:
                res += f"{self.x[0]} " if i == 0 else f"{self.x[i]:+}x^{i} "
        print(res[1:] if res[0] == '+' else res)

    def size(self):
        return len(self.x)


if __name__ == "__main__":
    p = Poly((1, 0, -2))
    p.print()
    q = p.power(2)
    q.print()
    q = p.power(3)
    q.print()
    # r = q.diff()
    # r.print()
    # s = r.integrate()
    # s.print()
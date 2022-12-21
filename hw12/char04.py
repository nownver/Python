import abc
import turtle as t

class Char(abc.ABC):
    def __init__(self, size):
        self.size = size

    @abc.abstractmethod
    def draw(self, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()

    def getWidth(self):
        return f"Width is {self.size}"
        

class Char0(Char):
    def __init__(self, size):
        super().__init__(size)

    def draw(self, x, y):
        super().draw(x, y)

        for i in range(2):
            t.fd(self.size)
            t.rt(90)
            t.fd(self.size * 2)
            t.rt(90)

class Char1(Char):
    def __init__(self, size):
        super().__init__(size)

    def draw(self, x, y):
        super().draw(x, y)

        t.fd(self.size/3)
        t.rt(90)
        t.fd(self.size*2)
        t.seth(0)
        t.fd(self.size/3)
        t.bk(self.size/1.5)
        t.seth(0)

class Char2(Char):
    def __init__(self, size):
        super().__init__(size)

    def draw(self, x, y):
        super().draw(x, y)

        t.fd(self.size)
        t.rt(90)
        t.fd(self.size)
        t.rt(90)
        t.fd(self.size)
        t.lt(90)
        t.fd(self.size)
        t.lt(90)
        t.fd(self.size)
        t.seth(0)

class Char3(Char):
    def __init__(self, size):
        super().__init__(size)

    def draw(self, x, y):
        super().draw(x, y)

        t.fd(self.size)
        t.rt(90)
        t.fd(self.size)
        t.rt(90)
        t.fd(self.size)
        t.bk(self.size)
        t.seth(270)
        t.fd(self.size)
        t.rt(90)
        t.fd(self.size)
        t.seth(0)

class Char4(Char):
    def __init__(self, size):
        super().__init__(size)

    def draw(self, x, y):
        super().draw(x, y)

        t.seth(270)
        t.fd(self.size)
        t.lt(90)
        t.fd(self.size + self.size/3)
        t.bk(self.size/3)
        t.lt(90)
        t.fd(self.size)
        t.bk(self.size*2)
        t.seth(0)

class Char5(Char):
    def __init__(self, size):
        super().__init__(size)

    def draw(self, x, y):
        super().draw(x, y)
        t.pu()
        t.fd(self.size + self.size/3)
        t.pd()

        t.bk(self.size)
        t.rt(90)
        t.fd(self.size)
        t.lt(90)
        t.fd(self.size)
        t.rt(90)
        t.fd(self.size)
        t.rt(90)
        t.fd(self.size)
        t.seth(0)

class Char6(Char):
    def __init__(self, size):
        super().__init__(size)

    def draw(self, x ,y):
        super().draw(x, y)
        t.pu()
        t.fd(40)
        t.pd()

        t.bk(self.size)
        t.rt(90)
        t.fd(self.size * 2)
        t.lt(90)
        t.fd(self.size)
        t.lt(90)
        t.fd(self.size)
        t.lt(90)
        t.fd(self.size)
        t.seth(0)

class Char7(Char):
    def __init__(self, size):
        super().__init__(size)

    def draw(self, x ,y):
        super().draw(x, y)

        t.fd(self.size)
        t.rt(105)
        t.fd(self.size * 2)
        t.bk(self.size)
        t.seth(0)
        t.fd(6)
        t.bk(self.size / 2)
        t.seth(0)

class Char8(Char):
    def __init__(self, size):
        super().__init__(size)

    def draw(self, x ,y):
        super().draw(x, y)

        for i in range(4):
            t.fd(self.size)
            t.rt(90)
        t.rt(90)
        t.fd(self.size)
        t.lt(90)
        for i in range(4):
            t.fd(self.size)
            t.rt(90)
        t.seth(0)

class Char9(Char):
    def __init__(self, size):
        super().__init__(size)

    def draw(self, x, y):
        super().draw(x, y)

        for i in range(4):
            t.fd(self.size)
            t.rt(90)
        t.rt(90)
        t.fd(self.size)
        t.lt(90)
        t.fd(self.size)
        t.rt(90)
        t.fd(self.size)
        t.rt(90)
        t.fd(self.size)
        t.seth(0)

zero = Char0(30)
  
one = Char1(30)

two = Char2(30)

three = Char3(30)

four = Char4(30)

five = Char5(30)

six = Char6(30)

seven = Char7(30)

eight = Char8(30)

nine = Char9(30)

num_dict = {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}

x = 0
y = 0
for i in num_dict:
    num_dict[i].draw(x,y)
    x += 50
    print(num_dict[i].getWidth())

t.done()
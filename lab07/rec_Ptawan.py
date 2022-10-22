# ID: 63011335
# Name: Tawan Lekngam
# LabNo: 07
# QNo: 03/1

from __future__ import annotations
import turtle as t


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, x=0, y=0, width=100, height=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bottom_left = Point(x, y - self.height)
        self.top_right = Point(x + self.width, y)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def draw(self, name=""):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.write(name)
        for _ in range(2):
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)
            t.right(90)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.bottom_left.move(x, y - self.height)
        self.top_right.move(x + self.width, y)

    def intersert(self, other: Rectangle) -> Rectangle:
        if self.is_overlap(other):
            x = max(self.bottom_left.x, other.bottom_left.x)
            y = min(self.top_right.y, other.top_right.y)
            width = min(self.top_right.x, other.top_right.x) - \
                max(self.bottom_left.x, other.bottom_left.x)
            height = min(self.top_right.y, other.top_right.y) - \
                max(self.bottom_left.y, other.bottom_left.y)
            if height > 0 and width > 0:
                return Rectangle(x, y, width, height)

    def is_overlap(self, other: Rectangle):
        return not (self.top_right.x < other.bottom_left.x or self.bottom_left.x > other.top_right.x or self.top_right.y < other.bottom_left.y or self.bottom_left.y > other.top_right.y)


if __name__ == "__main__":
    # a = Rectangle(90, 0, 100, 100)
    # # b = Rectangle(0, -60, 120, 70)
    # b = Rectangle(0, 60, 120, 60)
    a = Rectangle(0, 40, 100, 100)
    b = Rectangle(20, 150, 180, 120)
    c = a.intersert(b)
    a.draw("A")
    b.draw("B")
    try:
        t.color("red")
        c.draw("C")

    except Exception:
        pass
    t.mainloop()
    
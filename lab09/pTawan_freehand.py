from tkinter import *


class Freehand:
    def __init__(self):
        self.root = Tk()
        self.root.title("A simple paint program")
        self.x: float
        self.y: float 

        self.canvas = Canvas(self.root, width=300, height=200)
        self.canvas.grid(row=1)
        self.canvas.bind("<Button-1>", self.clickEvent)
        self.canvas.bind("<B1-Motion>", self.moveEvent)
        Label(self.root, text="Drag the mouse to draw").grid(row=2)
        Button(self.root, width=30, text="Clear",
               command=self.clear).grid(row=3)

    def clickEvent(self, event: Event):
        self.x = event.x
        self.y = event.y

    def moveEvent(self, event: Event):
        self.canvas.create_line(event.x, event.y, self.x, self.y, fill="#000",width=5)
        self.x = event.x
        self.y = event.y
        
    def clear(self):
        self.canvas.delete("all")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Freehand()
    app.run()

from tkinter import *
import tkinter.messagebox
import random

class Application:

    def __init__(self):
        self.root = Tk()

        self.canvas = Canvas(self.root, width=450, height=300)
        self.canvas.create_rectangle(50, 50, 400, 250)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.mouseEvent)

    def mouseEvent(self, event: Event):
        if not(50 <= event.x <= 400 and 50 <= event.y <= 250):
            tkinter.messagebox.showinfo(
                "Warning", "Mouse pointer is not in the rectangle")
            return

        color = ['purple', 'blue', 'green',
                 'yellow', 'orange', 'red', 'magenta']
        x1 = event.x - 2
        y1 = event.y - 2
        x2 = event.x + 2
        y2 = event.y + 2
        self.canvas.create_oval(
            x1, y1, x2, y2, fill=color[random.randint(0, 6)])

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()

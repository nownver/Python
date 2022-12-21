import random
from tkinter import *
import tkinter.messagebox

class Star:
    def __init__(self):
        self.root = Tk()
        self.root.title("Star")

        self.canvas = Canvas(self.root, width=450, height=300)
        self.canvas.pack()
        self.canvas.create_rectangle(50,50,400,250, tags="rect")


        self.canvas.bind("<Button-1>", self.draw_circle)
        

    def draw_circle(self, event):
        self.lastx = event.x
        self.lasty = event.y

        color = ['purple', 'blue', 'green', 'yellow', 'orange', 'red', 'magenta']
        if 50 <= self.lastx <= 400 and 50 <= self.lasty <= 250:
            self.canvas.create_oval(self.lastx-10, self.lasty-10, self.lastx+10, self.lasty+10, tags="oval", fill=color[random.randint(0,6)])
        else:
            tkinter.messagebox.showinfo("out of range", "Not in rect")



    # def find_event(self, event):
    #     self.lastx = event.x
    #     self.lasty = event.y

    def run(self):
        self.root.mainloop()

if __name__ == __name__:
    Star().run()
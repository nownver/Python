from tkinter import *
class Paint:
    def __init__(self):
        window = Tk()
        window.title("tk")
        self.canvas = Canvas(window, width = 450, height = 300,background="white")
        self.canvas.grid(row=0, column=0)
        self.canvas.bind('<Button-1>',self.create)
        self.canvas.bind('<Button-2>',self.Delete)
        window.mainloop()

    def create(self,event):
        x1=event.x
        y1=event.y
        x2=event.x
        y2=event.y
        self.canvas.create_oval(x1,y1,x2,y2,outline = "black",width=20)
    
    def Delete(self,event):
        nearest = self.canvas.find_closest(event.x,event.y)
        self.canvas.delete(nearest)
Paint()

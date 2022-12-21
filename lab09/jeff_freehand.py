# Question 3

from tkinter import *

class Paint:
    def __init__(self):
        window = Tk()
        window.title("A simple paint program")
        window.geometry("500x320")
        
        self.canvas = Canvas(window, width = 500, height = 250, bg = 'white')
        self.canvas.pack()
        
        self.label = Label(window, text = "Drag the mouse to draw")
        self.label.pack()
        
        self.button = Button(window, text = "Clear", command = self.clear)
        self.button.pack()
        
        self.canvas.bind("<Button 1>", self.get_pos)
        self.canvas.bind('<B1-Motion>', self.draw)
                
        window.mainloop()
        
    def get_pos(self, event):
        global x, y
        x = event.x
        y = event.y

    def draw(self, event):
        global x, y
        self.canvas.create_line((x, y, event.x, event.y), fill='black', width=5, tags = "drawing")
        x = event.x
        y = event.y
                    
    def clear(self):
        self.canvas.delete('drawing')

Paint()
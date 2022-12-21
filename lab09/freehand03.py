# from tkinter import *

# class Freehand:
#     def __init__(self):
#         window = Tk()
#         window.title("A simple paint program")

#         self.canvas = Canvas(window, width= 200, height = 100, bg = "white")
#         self.canvas.pack()

#         def paint(event):
#             x = event.x
#             y = event.y
#             canvas = event.widget
#             for i in range(SEEDS):
#                 random_x,random_y = random_point(x,y)
#                 canvas.create_line(random_x,random_y,random_x+1,random_y+1,fill='black')
            

import tkinter as tk
 
 
lastx, lasty = 0, 0
 
 
def xy(event):
    "Takes the coordinates of the mouse when you click the mouse"
    global lastx, lasty
    lastx, lasty = event.x, event.y
 
 
def addLine(event):
    """Creates a line when you drag the mouse
    from the point where you clicked the mouse to where the mouse is now"""
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    # this makes the new starting point of the drawing
    lastx, lasty = event.x, event.y
 
 
root = tk.Tk()
root.geometry("800x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = tk.Canvas(root)
canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
 
def clear():
    canvas.delete("all")

lb = tk.Label(root, text="Drag the mouse to draw")
lb.grid(column=0, row=10)
bt1 = tk.Button(root, text="Clear", command = clear)
bt1.grid(column=0, row=20)
root.mainloop()
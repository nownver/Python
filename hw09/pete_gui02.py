from tkinter import *
root = Tk()
root.geometry("200x180")
root.title("PROJECT GUI")

Label(text="Main Menu",font=("Calibri",20,"bold")).pack(anchor=N)
Button(text="Start",font=("Calbri",20,"bold")).pack(anchor=N)
Button(text="Settings",font=("Calbri",20,"bold")).pack(anchor=N)
Button(text="History",font=("Calbri",20,"bold")).pack(anchor=N)
Button(text="Exit",font=("Calbri",20,"bold")).pack(anchor=N)

root.mainloop()




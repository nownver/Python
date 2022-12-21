from tkinter import *
import tkinter.messagebox as tm
root = Tk()
root.title("KMITL Phone")
root.geometry("285x330")

num = ""
inp = StringVar()

def dial(b):
    global num
    num+=str(b)
    inp.set(num)
    
def dele():
    global num
    num = num[:-1]
    inp.set(num)

def call():
    global num
    tm.showinfo("Dialing...",f"Dialling<<{num}>>")

et1 = Entry(font=("Calibri",20,'bold'),textvariable=inp,justify="right")
et1.grid(columnspan=6)

b1 = Button(text=1,font=("Calibri",20,'bold'),padx=30,bg="orange",command=lambda:dial(1)).grid(row=1,column=0,columnspan=2)
b2 = Button(text=2,font=("Calibri",20,'bold'),padx=30,fg='orange',command=lambda:dial(2)).grid(row=1,column=2,columnspan=2)
b3 = Button(text=3,font=("Calibri",20,'bold'),padx=30,bg="orange",command=lambda:dial(3)).grid(row=1,column=4,columnspan=2)

b4 = Button(text=4,font=("Calibri",20,'bold'),padx=30,fg='orange',command=lambda:dial(4)).grid(row=2,column=0,columnspan=2)
b5 = Button(text=5,font=("Calibri",20,'bold'),padx=30,bg="orange",command=lambda:dial(5)).grid(row=2,column=2,columnspan=2)
b6 = Button(text=6,font=("Calibri",20,'bold'),padx=30,fg='orange',command=lambda:dial(6)).grid(row=2,column=4,columnspan=2)

b7 = Button(text=7,font=("Calibri",20,'bold'),padx=30,bg="orange",command=lambda:dial(7)).grid(row=3,column=0,columnspan=2)
b8 = Button(text=8,font=("Calibri",20,'bold'),padx=30,fg='orange',command=lambda:dial(8)).grid(row=3,column=2,columnspan=2)
b9 = Button(text=9,font=("Calibri",20,'bold'),padx=30,bg="orange",command=lambda:dial(9)).grid(row=3,column=4,columnspan=2)

bm = Button(text="*",font=("Calibri",20,'bold'),padx=30,fg='orange',command=lambda:dial("*")).grid(row=4,column=0,columnspan=2)
b0 = Button(text=0,font=("Calibri",20,'bold'),padx=30,bg="orange",command=lambda:dial(0)).grid(row=4,column=2,columnspan=2)
bs = Button(text="#",font=("Calibri",20,'bold'),padx=30,fg='orange',command=lambda:dial("#")).grid(row=4,column=4,columnspan=2)

bt = Button(text="Talk",font=("Calibri",20,'bold'),padx=40,bg="orange",command=call).grid(row=5,column=0,columnspan=3)
bd = Button(text="<",font=("Calibri",20,'bold'),padx=52,fg='orange',command=dele).grid(row=5,column=3,columnspan=3)

root.mainloop()

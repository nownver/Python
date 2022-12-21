from tkinter import *
from turtle import bgcolor

class CrypPre:
    def __init__(self):
        self.root = Tk()
        self.root.title("Crypto Price Prediction")
        self.root.geometry("255x275")

        number = Label(self.root, text = "Menu")
        number.grid(row=0,column=0)

        self.currency()

    def currency(self):
        self.frame1 = Frame(self.root)
        self.frame1.grid(column=0, row=1)

        bt1 = Button(self.frame1,text= "Exchange rate", width = 10, height = 3)
        bt1.grid(row=0,column=0,columnspan=3)

        bt2 = Button(self.frame1,text= "predict past period", width = 10, height = 3)
        bt2.grid(row=1,column=0,columnspan=1)

        bt3 = Button(self.frame1,text= "predict future", width = 10, height = 3)
        bt3.grid(row=2,column=0)


        bt4 = Button(self.frame1,text= "Popular coins", width = 10, height = 3)
        bt4.grid(row=0,column=4)

        bt4 = Button(self.frame1,text= "Calculator", width = 10, height = 3)
        bt4.grid(row=1,column=4)

        bt4 = Button(self.frame1,text= "History", width = 10, height = 3)
        bt4.grid(row=2,column=4)

        bt5 = Button(self.frame1,text= "Exit", width = 5, height = 1)
        bt5.grid(row=3,column=4)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    CrypPre().run()
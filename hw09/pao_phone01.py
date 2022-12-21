from tkinter import *
from tkinter import messagebox

class KMITL_Phone:
    def __init__(self):
       
        window = Tk()
        window.title("KMITL Phone")

        self.text = Entry(window,font = ("Helvetica", 19),justify="right")
        self.text.grid(row=1,column=0,columnspan=10)

        Button_1 = Button(window, width = 6, text = "1", font = ("Helvetica", 18),command = lambda: self.getnum(1))
        Button_1.grid(row = 2, column= 2,columnspan=2)

        Button_2 = Button(window, width = 6, text = "2", font = ("Helvetica", 18), command = lambda: self.getnum(2))
        Button_2.grid(row = 2, column= 4,columnspan=2)

        Button_3 = Button(window, width = 6, text = "3", font = ("Helvetica", 18), command = lambda: self.getnum(3))
        Button_3.grid(row = 2, column= 6,columnspan=2)

        Button_4 = Button(window, width = 6, text = "4", font = ("Helvetica", 18), command = lambda: self.getnum(4))
        Button_4.grid(row = 4, column= 2,columnspan=2)

        Button_5 = Button(window, width = 6, text = "5", font = ("Helvetica", 18), command = lambda: self.getnum(5))
        Button_5.grid(row = 4, column= 4,columnspan=2)

        Button_6 = Button(window, width = 6, text = "6", font = ("Helvetica", 18), command = lambda: self.getnum(6))
        Button_6.grid(row = 4, column= 6,columnspan=2)

        Button_7 = Button(window, width = 6, text = "7", font = ("Helvetica", 18), command = lambda: self.getnum(7))
        Button_7.grid(row = 6, column= 2,columnspan=2)

        Button_8 = Button(window, width = 6, text = "8", font = ("Helvetica", 18), command = lambda: self.getnum(8))
        Button_8.grid(row = 6, column= 4,columnspan=2)

        Button_9 = Button(window, width = 6, text = "9", font = ("Helvetica", 18), command = lambda: self.getnum(9))
        Button_9.grid(row = 6, column= 6,columnspan=2)

        Button_10 = Button(window, width = 6, text = "*", font = ("Helvetica", 18), command = lambda: self.getnum('*'))
        Button_10.grid(row = 8, column= 2,columnspan=2)

        Button_0 = Button(window, width = 6, text = "0", font = ("Helvetica", 18), command = lambda: self.getnum(0))
        Button_0.grid(row = 8, column= 4,columnspan=2)

        Button_U = Button(window, width = 6, text = "#", font = ("Helvetica", 18), command = lambda: self.getnum('#'))
        Button_U.grid(row = 8, column= 6,columnspan=2)

        Button_Talk = Button(window, width = 10, text = "Talk", font = ("Helvetica", 18), command = self.dial)
        Button_Talk.grid(row = 12, column= 3,columnspan=2)

        Button_minus = Button(window, width = 9, text = "<", font = ("Helvetica", 18), command = self.delete)
        Button_minus.grid(row = 12, column= 5,columnspan=2)

        window.mainloop()
    
    def getnum(self,number):
        number = str(number)
        self.text.insert('end', number)
        
    def dial(self):
        messagebox.showinfo("Dial",f"Dialling<<{self.text.get()}>>")

    def delete(self):
        euro = len(self.text.get())
        self.text.delete(euro-1)

KMITL_Phone()
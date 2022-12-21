from tkinter import *

class Money:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")


        # frame1 = Frame(window)
        # frame1.pack()
        num = DoubleVar()
        entryNum = Entry(window, textvariable= num)
        entryNum.pack()
        # number = Label(window, text = 0)
        # number.pack()

        def thbToUsd():
            # entryNum["text"] = int(entryNum["textvariable"]).get() / 30
            # num.set(num.get() / 30)
            print(num)
            wd2 = Tk()
            wd2.title("tk")
            lb1 = Label(wd2, text = f"{num.get() / 30:.2f} USD = {num.get()} THB")
            lb1.pack()
            wd2.mainloop()

        def usdToThb():
            # num.set(num.get() * 30)
            print(num)
            wd2 = Tk()
            wd2.title("tk")
            lb1 = Label(wd2, text = f"{num.get() * 30:.2f} THB = {num.get()} USD")
            lb1.pack()
            wd2.mainloop()

        btThbtoUsd = Button(window, text = "THB -> USD", command= thbToUsd)
        btThbtoUsd.pack()

        btUsdtoThb = Button(window, text = "USD -> THB", command= usdToThb)
        btUsdtoThb.pack()
        
        window.mainloop()
Money()


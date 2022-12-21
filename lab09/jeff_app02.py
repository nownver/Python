# Question 2

from tkinter import *

window = Tk()
window.title("Currency Converter")
window.geometry("300x200")

def toTHB():
    thb = int(box.get()) * 30
    thb = "{:.2f}".format(thb)
    thbWindow = Tk()
    thbWindow.title("USD to THB")
    thbWindow.geometry("300x200")
    
    displayTHB = Label(thbWindow, text = f"{box.get()} USD = {thb} THB")
    displayTHB.pack(pady=50)
    
    btOK = Button(thbWindow, text = "OK", command = thbWindow.destroy)
    btOK.pack()
    
    thbWindow.mainloop()
    
def toUSD():
    usd = int(box.get()) / 30
    usd = "{:.2f}".format(usd)
    usdWindow = Tk()
    usdWindow.title("THB to USD")
    usdWindow.geometry("300x200")
    displayUSD = Label(usdWindow, text = f"{box.get()} THB = {usd} USD")
    displayUSD.pack(pady=50)
    
    btOK = Button(usdWindow, text = "OK", command = usdWindow.destroy)
    btOK.pack()
    
    usdWindow.mainloop()
    

box = StringVar()
entry = Entry(window, textvariable = box)
entry.insert(0,0)
entry.pack(pady=40)

btTHB = Button(window, text = "USD -> THB", command = toTHB)
btTHB.pack()
btUSD = Button(window, text = "THB -> USD", command = toUSD)
btUSD.pack()
    

window.mainloop()
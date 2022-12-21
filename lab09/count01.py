from tkinter import *

class Count:
    def __init__(self):
        window = Tk()
        window.title("Spinner")

        number = Label(window, text = 0)
        number.pack()

        def countUp():
            number["text"] = number["text"] + 1

        def countDown():
            number["text"] = number["text"] - 1

        def reset():
            number["text"] = 0

        bt1 = Button(window, text="+", command = lambda: countUp())
        bt2 = Button(window, text="-", command = lambda: countDown())
        bt3 = Button(window, text="reset", command = lambda: reset())
        bt1.pack()
        bt2.pack()
        bt3.pack()

        window.mainloop()


Count()
from tkinter import *


class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title("spinner")

        self.value = IntVar(self.root)

        Label(self.root, textvariable=self.value, width=10).grid(
            column=0, row=0, rowspan=3)

        btn_width = 6
        Button(self.root, text="+", width=btn_width,
               command=lambda: self.value.set(self.value.get() + 1)).grid(column=1, row=0, sticky="e")
        Button(self.root, text="-", width=btn_width,
               command=lambda: self.value.set(self.value.get() - 1)).grid(column=1, row=1, sticky="e")
        Button(self.root, text="reset", width=btn_width,
               command=lambda: self.value.set(0)).grid(column=1, row=2, sticky="e")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
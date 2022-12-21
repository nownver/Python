import tkinter as tk
from tkinter import messagebox


class Application:
    
    def __init__(self):
        self.root = tk.Tk()
        self.value = tk.DoubleVar(self.root)
        tk.Entry(self.root, textvariable=self.value).pack()
        tk.Button(self.root, text="USD -> THB", command=lambda:self.to_thb()).pack()
        tk.Button(self.root, text="THB -> USD", command=lambda: self.to_usd()).pack()

    def to_thb(self):
        messagebox.Message(self.root,
                           title="USD -> THB",
                           message=f"{self.value.get():.2f} USD = {self.value.get() * 30:.2f} THB").show()

    def to_usd(self):
        messagebox.Message(self.root,
                           title="THB -> USD",
                           message=f"{self.value.get():.2f} USD = {self.value.get() / 30:.2f} THB").show()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()

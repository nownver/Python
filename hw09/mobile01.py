
from tkinter import *
from tkinter.font import BOLD
import tkinter.messagebox

class Phone:
    def __init__(self):
        self.window = Tk()
        self.window.title("KMITL Phone")
        self.window.geometry("400x375")

        #display
        self.frame0 = Frame(self.window)
        self.frame0.grid(column=0, row=0)
        self.value = ''
        self.label = Label(self.frame0, text = self.value, width = 30, height = 3)
        self.label.grid(row=0,column=0,padx=62.5)
        
        #123
        self.frame1 = Frame(self.window)
        self.frame1.grid(column=0, row=1)
        bt1 = Button(self.frame1,text= "1",command = lambda: self.click('1'), width = 10, height = 3)
        bt1.grid(row=0,column=0)

        bt2 = Button(self.frame1,text= "2",command = lambda: self.click('2'), width = 10, height = 3)
        bt2.grid(row=0,column=1)

        bt3 = Button(self.frame1,text= "3",command = lambda: self.click('3'), width = 10, height = 3)
        bt3.grid(row=0,column=2)

        #456
        self.frame2 = Frame(self.window)
        self.frame2.grid(column=0, row=2)
        bt4 = Button(self.frame2,text= "4",command = lambda: self.click('4'), width = 10, height = 3)
        bt4.grid(row=1,column=0)

        bt5 = Button(self.frame2,text= "5",command = lambda: self.click('5'), width = 10, height = 3)
        bt5.grid(row=1,column=1)

        bt6 = Button(self.frame2,text= "6",command = lambda: self.click('6'), width = 10, height = 3)
        bt6.grid(row=1,column=2)

        #789
        self.frame3 = Frame(self.window)
        self.frame3.grid(column=0, row=3)
        bt7 = Button(self.frame3,text= "7",command = lambda: self.click('7'), width = 10, height = 3)
        bt7.grid(row=2,column=0)

        bt8 = Button(self.frame3,text= "8",command = lambda: self.click('8'), width = 10, height = 3)
        bt8.grid(row=2,column=1)

        bt9 = Button(self.frame3,text= "9",command = lambda: self.click('9'), width = 10, height = 3)
        bt9.grid(row=2,column=2)

        #*0#
        self.frame4 = Frame(self.window)
        self.frame4.grid(column=0, row=4)
        btAstRsk = Button(self.frame4,text= "*",command = lambda: self.click('*'), width = 10, height = 3)
        btAstRsk.grid(row=3,column=0)

        bt0 = Button(self.frame4,text= "0",command = lambda: self.click('0'), width = 10, height = 3)
        bt0.grid(row=3,column=1)

        btHash = Button(self.frame4,text= "#",command = lambda: self.click('#'), width = 10, height = 3)
        btHash.grid(row=3,column=2)

        #talk<
        self.frame5 = Frame(self.window)
        self.frame5.grid(column=0, row=5)
        btTalk = Button(self.frame5,text= "Talk",command = lambda: self.talk(), width = 17, height = 3)
        btTalk.grid(row=4,column=0)

        btDelete = Button(self.frame5,text= "<",command = lambda: self.delete(), width = 17, height = 3)
        btDelete.grid(row=4,column=1)


    def run(self):
        self.window.mainloop()

    def click(self, n):
        self.n = n
        # self.value = self.n
        self.label["text"] += self.n
        print(self.n)

    def talk(self):
        tkinter.messagebox.showinfo("showinfo", f'Dialling {self.label["text"]}')

    def delete(self):
        self.label["text"] = self.label["text"][:-1]


if __name__ == "__main__":
    Phone().run()
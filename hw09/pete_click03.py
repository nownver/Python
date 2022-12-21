from tkinter import *

root = Tk()
root.title("tk")
root.geometry("800x800")
canva = Canvas(root,width=800,height=800)
canva.pack()

i=0
t=0
posit = {}

def click(pos):
    global x,i,t
    i+=1
    t+=1
    x=canva.create_oval(pos.x,pos.y,pos.x+100,pos.y+100,tags=str(t))  
    posit[i]=[pos.x,pos.y,pos.x+100,pos.y+100,str(t)]
    
def delete(pos):
    for i in posit:
        if posit[i][0]<pos.x<posit[i][2] and posit[i][1]<pos.y<posit[i][3]:
            canva.delete(posit[i][4])

canva.bind("<Button-1>",click)
canva.bind("<Button-2>",delete)  #<Button-3> is my right-click

root.mainloop()
from tkinter import *

def pie_chart(lst):
    table = {}
    sum = 0
    for c in lst:
        c_count = lst.count(c)
        table[c] = c_count

    print(table)
    for k,v in list(table.items()):
        sum += v
    print(sum)

    def find_angle(n):
        return 360 * n / sum

    color = ["purple", "green", "red", "yellow", "pink", "brown", "black", "blue", "grey", "brown"]
    root = Tk()
    canvas = Canvas(root, width=300, height=300)
    canvas.pack()

    a = 0
    i = 0
    for k,v in sorted(table.items()):
        canvas.create_arc((50,50,250,250), fill = color[i%10], outline="white", start =find_angle(a), extent=find_angle(v))
        a += v
        i += 1

    root.mainloop()

print(pie_chart([3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3]))

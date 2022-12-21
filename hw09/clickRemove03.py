# from tkinter import *

# class ClickRemove:
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("ClickRemove")

#         self.canvas = Canvas(self.root, width=450, height=300)
#         self.canvas.pack()

#         self.canvas.bind("<Button-1>", self.draw_circle)
#         self.canvas.bind("<Button-2>", self.delete_circle)

#         self.clicked_x = []
#         self.clicked_y = []
        
#     def draw_circle(self, event):
#         self.lastx = event.x
#         self.lasty = event.y

#         self.canvas.create_oval(self.lastx-10, self.lasty-10, self.lastx+10, self.lasty+10, tags=f"oval{self.lastx}{self.lasty}")
#         print(f"oval{self.lastx},{self.lasty}")

#         self.clicked_x.append(self.lastx)
#         self.clicked_y.append(self.lasty)

#     def delete_circle(self,event):
#         self.dlastx = event.x
#         self.dlasty = event.y

#         range_x = []
#         for i in self.clicked_x:
#             range_x.append(list(range(i-10,i+10)))

#         range_y = []
#         for i in self.clicked_y:
#             range_y.append(list(range(i-10,i+10)))

#         for i in range(len(range_x)):
#             if self.dlastx in range_x[i] and self.dlasty in range_y[i]:
#                 self.canvas.delete(f"oval{range_x[i][0]+10}{range_y[i][0]+10}")
#                 print(f"doval{range_x[i][0]+10},{range_y[i][0]+10}")
#                 # self.canvas.delete("all")

#     def run(self):
#         self.root.mainloop()


# if __name__ == "__main__":
#     ClickRemove().run()





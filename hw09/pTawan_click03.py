import tkinter as tk


class Application:

    def __init__(self, root=tk.Tk()):
        self.root = root
        self.tag_no = 0
        self.canvas = tk.Canvas(self.root, width=500, height=400)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.create_circle)
        self.canvas.bind("<Button-2>", self.remove_circle)

    def create_circle(self, e: tk.Event):
        self.canvas.create_oval(e.x - 20, e.y-20, e.x+20,
                                e.y+20, tags=str(self.tag_no))
        self.tag_no += 1

    def remove_circle(self, e: tk.Event):
        near_tag = self.canvas.find_overlapping(e.x-1, e.y-1, e.x+1, e.y+1)
        print(near_tag)
        self.canvas.delete(near_tag[0])

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
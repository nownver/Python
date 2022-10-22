import turtle as t 
import calendar as c 

t.speed(0) 
t.hideturtle() 
t.speed(0)
def draw_calendar(year: int): 
    x, y = (-400, 300) # initial point 
    size = 18  # setup 

    def draw_square(txt): 
        if txt != 0: 
            t.write(f" {txt}") 
        for _ in range(4): 
            t.forward(size) 
            t.left(90)

    t.penup() 
    t.goto(x, y) 
    for mm in range(12): 
        if mm % 3 == 0 and mm != 0: 
            t.goto(t.position()[0] + size * 8, y) 
        t.pendown() 
        t.write(f" Month#{mm+1}") # draw month header 
        for _ in range(2): 
            t.forward(size * 7) 
            t.left(90) 
            t.forward(size) 
            t.left(90) 
        t.goto(t.pos() + (0, -size)) 
        month_data = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"] 
        month_data.extend(c.TextCalendar(c.SUNDAY).itermonthdays(year, mm + 1)) 
        count = 0 
        for data in month_data: # draw month data 
            count += 1 
            t.pendown() 
            draw_square(data) 
            t.forward(size) 
            if count % 7 == 0: 
                t.penup() 
                t.goto(t.pos() + (-size * 7, -size)) 
        t.goto(t.pos() + (0, -size)) 


# if __ name __== "main": 
draw_calendar(2022) 
t.done()



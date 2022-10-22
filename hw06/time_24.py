def time24To12hour(time):
    sigh = "AM"
    if len(time) == 5:
        hour = time[0:2]
        min = time[3:5]
    elif len(time) == 4:
        hour = time[0:1]
        min = time[2:4]
    h = int(hour)
    m = int(min)
    if 0 <= h < 24 and 0 <= m < 60: 
        if h == 0:
            sigh = "AM"
            h = 12
        elif h == 12:
            sigh = "PM"
        elif h > 12:
            h = h - 12
            sigh = "PM"
        if len(str(h)) < 2:
            h = "0" + str(h)
        result = str(h) + ":" + min + " " + sigh
    return result

time_format = time24To12hour("23:24")
print(time_format)







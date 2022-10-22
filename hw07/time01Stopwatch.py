class Clock():
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def setTime(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def getTime(self):
        if 0 <= self.hour and 0 <= self.minute and 0 <= self.second :
            if self.second >= 60:
                self.minute += self.second // 60
                self.second = self.second % 60
            if self.minute >= 60:
                self.hour += self.minute // 60
                self.minute = self.minute % 60
            return self.hour, self.minute, self.second
        else:
            return False

    def tick(self):
        self.second = self.second + 1
        if self.second == 60:
            self.second = 0
            self.minute = self.minute + 1
        if self.minute ==60:
            self.minute = 0
            self.hour += 1

    def Display12Format(self):
        sign = "AM"
        if 0 <= self.hour < 24 and 0 <= self.minute < 60 and 0 <= self.second < 60:
            if self.hour == 0:
                sign = "PM"
                self.hour = 12
            elif self.hour == 12:
                sign = "AM"
            elif self.hour > 12:
                sign = "PM"
                self.hour = self.hour - 12

            if len(str(self.hour)) == 1:
                self.hour = "0" + str(self.hour)
            if len(str(self.minute)) == 1:
                self.minute = "0" + str(self.minute)
            if len(str(self.second)) == 1:
                self.second = "0" + str(self.second)
            
            print(f"{self.hour}:{self.minute}:{self.second} {sign}")
            

time1 = Clock()
time1.setTime(23,179,125)

a = time1.getTime()
print(a)
time1.tick()
time1.Display12Format()

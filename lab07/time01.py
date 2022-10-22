

class Time():
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec
        # print("u")
    def print(self):
        if 0 <= self.hour and 0 <= self.min and 0 <= self.sec:
            if self.sec >= 60:
                self.min = self.min + self.sec // 60
                self.sec = self.sec % 60
            if self.min >= 60:
                self.hour = self.hour + self.min // 60
                self.min = self.min % 60

            if len(str(self.hour)) == 1:
                self.hour = "0" + str(self.hour)
            if len(str(self.min)) == 1:
                self.min = "0" + str(self.min)
            if len(str(self.sec)) == 1:
                self.sec = "0" + str(self.sec)
            
            print(f"{self.hour}:{self.min}:{self.sec} Hrs.")
        # else:
        #     print("nope")

time1 = Time(9,300,70)
time1.print()


    
    
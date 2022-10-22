

#------------- wrong-------------------
class Clock:
    def __init__(self, h = 0, m = 0, s = 0):
        self.__h = h
        self.__m = m
        self.__s = s
        self.check()
    def setTime(self,newH,newM,newS):
        self.__h = newH
        self.__m = newM
        self.__s = newS
        self.check()

    def getTime(self):
        return self.__h,self.__m,self.__s
    
    def check(self):
        if self.__h<0 or self.__m<0 or self.__s<0:
            raise (ValueError("Time Error"))
        if self.__s >=60:
            self.__m += self.__s//60
            self.__s %=60
        if self.__m >=60:
            self.__h += self.__m//60
            self.__m %=60
        if self.__h >=24:
            self.__h %=24

    def tick(self):
        self.__s += 1
        self.check()
    
    def display(self,f= 24):
        if(f == 24):
            print("{:02d}:{:02d}:{:02d}".format(self.__h,self.__m,self.__s))
        elif f == 12:
            if(self.__h>=12):
                print("{:02d}:{:02d}:{:02d} PM".format(self.__h-12,self.__m,self.__s))
            else:
                print("{:02d}:{:02d}:{:02d} AM".format(self.__h,self.__m,self.__s))


c1 = Clock()
c1.setTime(0,0,0)
# c1.tick()
c1.display()
c1.display(12)


# c1.setTime(23,59,59)
# c1.display()
# c1.display(12)
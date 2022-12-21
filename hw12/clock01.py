from datetime import datetime, timedelta
import time

now = datetime.now()

class Clock:
    def __init__(self, hh=now.hour, mm=now.minute, ss=now.second):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def run(self):
        flag = True
        while flag:
            self.realTime = (datetime.now() + timedelta(seconds=1)).strftime('%H:%M:%S')
            time.sleep(1)
            print(self.realTime)
 
    def setTime(self, h, m, s):
        self.hh = h
        self.mm = m
        self.ss = s

class AlarmClock(Clock):
    def __init__(self, alarm_hh, alarm_mm, alarm_ss, alarm_on_off=False, hh=now.hour, mm=now.minute, ss=now.second):
        super().__init__(hh,mm,ss)

        self.alarm_hh = alarm_hh
        self.alarm_mm = alarm_mm
        self.alarm_ss = alarm_ss
        self.alarm_on_off = alarm_on_off
    
    def setTime(self, h, m, s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s

    def alarm_on(self):
        self.alarm_on_off = True

    def alarm_off(self):
        self.alarm_on_off = False

    def run(self):
        if self.alarm_on_off == True:
            if 0 <= self.alarm_hh < 24 and 0 <= self.alarm_mm < 60 and 0 <= self.alarm_ss < 60:

                self.alarm_hh = self.alarm_hh if len(str(self.alarm_hh)) != 1 else f'0{self.alarm_hh}'
                self.alarm_mm = self.alarm_mm if len(str(self.alarm_mm)) != 1 else f'0{self.alarm_mm}'
                self.alarm_ss = self.alarm_ss if len(str(self.alarm_ss)) != 1 else f'0{self.alarm_ss}'

                alarmTime = f"{self.alarm_hh}:{self.alarm_mm}:{self.alarm_ss}"
                print(f"alarm time: {alarmTime}")
            else:
                raise ValueError("invalid alarm time")
  
            flag = True
            while flag:
                self.realTime = (datetime.now() + timedelta(seconds=1)).strftime('%H:%M:%S')
                time.sleep(1)
                print(self.realTime)
                if self.realTime == alarmTime:
                    print("Alarm Time!")
                    break

b = AlarmClock(20,49,5,True)
b.run()
from time import sleep
from datetime import datetime

now=datetime.now()

now_hours=now.hour
now_minutes=now.minute
now_seconds=now.second

changestep=int(input(f'Proovide step for time counting: '))
step_sleep=int(input('Provide countimg delay in seconds (min 1): '))
final_time=input('Provide final time in foramt hh:mm:ss: ')


class Timer:
    def __init__ (self, time_format, starttime, stoptime):
        self.time_format = time_format
        self.starttime = self.parse_time(starttime)
        self.stoptime= self.parse_time(stoptime)
        self.currenttime= self.starttime

    def parse_time(self, time_str):
        h,m,s=map(int, time_str.split(':'))
        return h*3600 + m*60 + s

    def format_time(self, seconds):
        h=seconds//3600
        m=(seconds%3600)//60
        s=seconds%60
        return f'{h:02}:{m:02}:{s:02}'

    def print_time(self):
        print(f'Current time is {self.format_time(self.currenttime)}')

    def increase_time(self):
        global changestep
        self.currenttime+=changestep

    def decrease_time(self):
        global changestep
        self.currenttime-=changestep

    def start(self):
        print(f'Starting the timer for {self.stoptime-self.starttime} seconds')
        while self.currenttime<self.stoptime:
            global step_sleep
            self.print_time()
            self.increase_time()
            sleep(step_sleep)
        print(f"Process finished, time counted down.")



final_time_parsed = Timer("hh:mm:ss", "00:00:00", final_time).parse_time(final_time)
final_fullyedited_time = Timer("hh:mm:ss", "00:00:00", final_time).format_time(final_time_parsed)


t=Timer("hh:mm:ss", f"{now_hours:02}:{now_minutes:02}:{now_seconds:02}", final_fullyedited_time)
t.start()
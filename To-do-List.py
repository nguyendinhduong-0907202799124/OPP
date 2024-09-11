from datetime import datetime

class Take:
    def __init__(self, name: str, jod: str, start_time: str, end_time: str, status: str):
        date_format = "%d/%m/%Y"
        self.name = name
        self.jod = jod
        self.start_time = datetime.strptime(start_time, date_format)
        self.end_time = datetime.strptime(end_time, date_format)
        self.status = status
        
        self.time1 = (self.end_time - self.start_time).days

    def now_times(self, now_time: str):
        date_format = "%d/%m/%Y"
        now_time = datetime.strptime(now_time, date_format)
        self.time2 = (now_time - self.start_time).days

    def prioritys(self, priority: str):
        self.priority = priority
        if self.time1 > 0:
            if self.time2 >= self.time1 * (1/3) and self.time2 < self.time1 * (1/2):
                return self.priority == "1"
            elif self.time2 >= self.time1 * (1/2) and self.time2 < self.time1 * (2/3):
                return self.priority == "2"
            elif self.time2 >= self.time1 * (2/3) and self.time2 <= self.time1:
                return self.priority == "3"
        elif self.time1 == 0:
            return f'{self.name}: {self.jod} needs to be comlepted today'
        else:
            return f'{self.name}: {self.jod} has been overdue'

    def get_status(self):
        if "complete" in self.status:
            return f'{self.name}: {self.jod} has been completed'
        else:
            return f'{self.name}: {self.jod} is still in progress'

    def __repr__(self):
        return f'Name: {self.name}, Job: {self.jod}, Priority: {self.priority}, Status: {self.status}'


class ChangeTake:
    
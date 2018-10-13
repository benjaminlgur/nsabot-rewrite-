import datetime
import time

def out_week_day():
    numeric = datetime.datetime.today().weekday()
    if numeric == 0:
        return "Monday"
    elif numeric == 1:
        return "Tuesday"
    elif numeric == 2:
        return "Wendsday"
    elif numeric == 3:
        return "Thursday"
    elif numeric == 4:
        return "Friday"
    elif numeric == 5:
        return "Saturday"
    elif numeric == 6:
        return "Sunday"

def out_date():
    return datetime.datetime.today().strftime('%Y-%m-%d')

def out_time():
    return time.strftime('%H:%M:%S')

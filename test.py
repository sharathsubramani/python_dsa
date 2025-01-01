import pytz
import datetime


def format_date(time):
    est = pytz.timezone('US/Eastern')
    fmt= '%Y-%m-%d %H:%M:%S'
    time = datetime(time)
    print(time.astimezone(est).strftime(fmt))
    
    
format_date('2024-11-23 02:27:12')
    
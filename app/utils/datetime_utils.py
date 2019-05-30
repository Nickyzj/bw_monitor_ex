from datetime import datetime

import pytz
from dateutil import tz

def convert_str_to_date(date_str):
    try:
        myDate = datetime.strptime(date_str, "%Y%m%d")
        return myDate.strftime("%Y-%m-%d")
    except ValueError as e:
        return ''

def convert_str_to_time(time_str):
    try:
        myTime = datetime.strptime(time_str, "%H%M%S")
        return myTime.strftime("%H:%M:%S")
    except ValueError as e:
        return ''

def get_tzlocal_now():
    return datetime.now(tz.tzlocal())

def convert_local_to_mst(local_now_time):
    to_zone = tz.gettz("America/Phoenix")

    return local_now_time.astimezone(to_zone)

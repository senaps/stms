import time
import datetime

import jdatetime


def get_current_timestamp():
    return int(time.time())


def jalali_time(timestamp):
    return jdatetime.datetime.utcfromtimestamp(timestamp=timestamp)

def jalali_datetime(datetime_stamp):
    return jdatetime.datetime.fromgregorian(datetime_stmap)
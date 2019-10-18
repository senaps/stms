import time
import datetime

import jdatetime


def jalali_time(timestamp):
    return jdatetime.datetime.utcfromtimestamp(timestamp=timestamp)

def jalali_datetime(datetime_stamp):
    return jdatetime.datetime.fromgregorian(datetime_stmap)
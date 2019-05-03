import time
import datetime

import jdatetime


def get_current_timestamp():
    return int(time.time())


def jalali_time(timestamp):
    jdatetime.datetime.utcfromtimestamp(timestamp=timestamp)
import datetime as dt
import logging
from urllib.request import urlopen


def load_leap_seconds():
    '''Loads the historical record of leap seconds from the Time Service Dept.
    of the US Naval Observatory

    Parameters
    ----------
    None

    Returns
    -------
    leap_seconds
        A list of tuples containing the python datetime and total number of
        leap seconds for each leap second addition
        Example:
        [(datetime1, 25.0), (datetime2, 26.0)]

    '''
    # documentation for leap seconds http://tycho.usno.navy.mil/leapsec.html
    url = 'http://maia.usno.navy.mil/ser7/tai-utc.dat'
    leap_seconds = []
    with urlopen(url) as f:
        for line in f:
            data = line.decode('utf-8').split()
            day = data[2] if len(data[2]) == 2 else '0' + data[2]
            date_str = data[0] + data[1] + day
            date = dt.datetime.strptime(date_str, '%Y%b%d')
            # gps was sychronized with utc on 1980-01-06 at which
            # point there were already 19 leap seconds
            leap_seconds.append((date, float(data[6]) - 19))

    return leap_seconds


LEAP_SECONDS = load_leap_seconds()


def _gps_time_parts(gps_time):
    h = int(gps_time / 1e4)
    m = int((gps_time % 1e4) / 100)
    s = int(gps_time % 100)
    ms = int((gps_time % 1) * 1000)

    return (h, m, s, ms)


def leap_seconds(dt):
    '''
    search the historical leap second record to find in the correct number of
    leap seconds to apply to the given datetime
    Parameters
    ----------
    dt (type: datetime)
        datetime for which to find the correct number of leap seconds

    Returns
    -------
    leap_seconds (type: float)
        number of leap seconds
    '''
    idx = len(LEAP_SECONDS) - 1
    # start at the end of the list becuase most data falls later in the 1961 - present record
    while LEAP_SECONDS[idx][0] > dt:
        idx -= 1
    leap_seconds = LEAP_SECONDS[idx][1]
    return leap_seconds


def gps_to_utc(date, gps_time):
    """Convert the GPS time on a given date into a UTC datetime.

    Parameters
    ----------
    date
        The date (datetime.date) on which the gps_time is referenced.
    gps_time
        The GPS time (float) for the given date. E.g., 12:34:56.789
        is the floating point number 123456.789.

    Returns
    -------
    datetime
        A datetime (datetime.datetime) in UTC for the given date and gps_time.
    """

    hours, minutes, seconds, milliseconds = _gps_time_parts(gps_time)
    if (seconds > 59):
        msg = 'Invalid gps_time on {0}: {1}.'.format(date, gps_time)
        logging.warning(msg)
        milliseconds = 0
        seconds = 0
        minutes = (minutes + 1) % 60
        if minutes == 0:
            hours = (hours + 1) % 24
        if hours == 0:
            date = date + dt.timedelta(days=1)
        msg = 'Corrected to {0} {1}:{2}:{3}.{4}.'.format(date, hours, minutes,
                                                         seconds, milliseconds)
        logging.warning(msg)
    gps_dt = dt.datetime(date.year, date.month, date.day,
                         hour=hours, minute=minutes,
                         second=seconds, microsecond=milliseconds*1000)
    utc_dt = gps_dt - dt.timedelta(seconds=leap_seconds(gps_dt))

    return utc_dt

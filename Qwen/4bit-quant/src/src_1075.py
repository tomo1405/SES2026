import pytz
from dateutil.parser import parse
# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_string, from_tz, to_tz):
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    dt = parse(time_string, dayfirst=True)
    dt = from_zone.localize(dt)
    dt = dt.astimezone(to_zone)

    return dt.strftime(TIME_FORMAT)
from random import choice
import pytz
from dateutil.parser import parse
# Constants
TIMEZONES = ['America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo', 'Australia/Sydney']
def task_func(date_str, from_tz):
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(choice(TIMEZONES))
    given_date = parse(date_str).replace(tzinfo=from_tz)
    converted_date = given_date.astimezone(to_tz)

    return converted_date.strftime('%Y-%m-%d %H:%M:%S'), to_tz.zone
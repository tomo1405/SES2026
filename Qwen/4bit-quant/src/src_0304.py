import pytz
import numpy as np
from dateutil.parser import parse
import math
MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])
def task_func(date_str, from_tz, to_tz):
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    given_date = parse(date_str).replace(tzinfo=from_tz)
    converted_date = given_date.astimezone(to_tz)

    moon_phase_year = MOON_PHASES_YEARS[np.argmin(np.abs(MOON_PHASES_YEARS - converted_date.year))]
    years_since_moon_phase_year = abs(converted_date.year - moon_phase_year)

    moon_phase = math.sin(math.pi * years_since_moon_phase_year / 7)

    return moon_phase
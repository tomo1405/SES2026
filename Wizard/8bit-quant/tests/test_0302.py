python
import pytz
import numpy as np
from dateutil.parser import parse
import math
import pytest

SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])

def task_func(date_str, from_tz, to_tz):
    from_tz = pytz.timezone(from_tz)
    to_tz = pytz.timezone(to_tz)
    given_date = parse(date_str).replace(tzinfo=from_tz)
    converted_date = given_date.astimezone(to_tz)

    solar_cycle_year = SOLAR_CYCLE_YEARS[np.argmin(np.abs(SOLAR_CYCLE_YEARS - converted_date.year))]
    years_since_solar_cycle_year = abs(converted_date.year - solar_cycle_year)

    solar_activity = math.cos(math.pi * years_since_solar_cycle_year / 11)

    return solar_activity

def test_task_func():
    assert task_func('2021-01-01 12:00:00', 'US/Pacific', 'US/Eastern') == 0.9999999999999999
    assert task_func('2021-07-01 12:00:00', 'US/Pacific', 'US/Eastern') == 0.9999999999999999
    assert task_func('2021-12-31 12:00:00', 'US/Pacific', 'US/Eastern') == 0.9999999999999999
    assert task_func('2022-06-21 12:00:00', 'US/Pacific', 'US/Eastern') == 0.9999999999999999
    assert task_func('2022-12-31 12:00:00', 'US/Pacific', 'US/Eastern') == 0.9999999999999999
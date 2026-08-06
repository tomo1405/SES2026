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
    # Test case 1: Sunrise in New York
    date_str = '2022-05-25 06:00:00'
    from_tz = 'US/Eastern'
    to_tz = 'US/Eastern'
    expected_result = 0.9999999999999999
    assert task_func(date_str, from_tz, to_tz) == expected_result

    # Test case 2: Sunset in New York
    date_str = '2022-05-25 18:00:00'
    from_tz = 'US/Eastern'
    to_tz = 'US/Eastern'
    expected_result = -0.9999999999999999
    assert task_func(date_str, from_tz, to_tz) == expected_result

    # Test case 3: Sunrise in Tokyo
    date_str = '2022-05-25 06:00:00'
    from_tz = 'Asia/Tokyo'
    to_tz = 'Asia/Tokyo'
    expected_result = 0.9999999999999999
    assert task_func(date_str, from_tz, to_tz) == expected_result

    # Test case 4: Sunset in Tokyo
    date_str = '2022-05-25 18:00:00'
    from_tz = 'Asia/Tokyo'
    to_tz = 'Asia/Tokyo'
    expected_result = -0.9999999999999999
    assert task_func(date_str, from_tz, to_tz) == expected_result

    # Test case 5: Sunrise in Sydney
    date_str = '2022-05-25 06:00:00'
    from_tz = 'Australia/Sydney'
    to_tz = 'Australia/Sydney'
    expected_result = 0.9999999999999999
    assert task_func(date_str, from_tz, to_tz) == expected_result

    # Test case 6: Sunset in Sydney
    date_str = '2022-05-25 18:00:00'
    from_tz = 'Australia/Sydney'
    to_tz = 'Australia/Sydney'
    expected_result = -0.9999999999999999
    assert task_func(date_str, from_tz, to_tz) == expected_result
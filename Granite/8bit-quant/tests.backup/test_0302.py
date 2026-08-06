import pytz
import numpy as np
from dateutil.parser import parse
import math
from src_0302 import task_func
SOLAR_CYCLE_YEARS = np.array([1986, 1996, 2008, 2019])

def test_task_func():
    date_str = "2022-01-01"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_result = math.cos(math.pi * 4 / 11)
    result = task_func(date_str, from_tz, to_tz)
    assert result == expected_result

def test_task_func_with_different_input():
    date_str = "2020-01-01"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_result = math.cos(math.pi * 2 / 11)
    result = task_func(date_str, from_tz, to_tz)
    assert result == expected_result
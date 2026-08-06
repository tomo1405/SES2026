import pytz
import numpy as np
from dateutil.parser import parse
import math
from src_0304 import task_func
MOON_PHASES_YEARS = np.array([1987, 1994, 2001, 2008, 2015, 2022])

def test_task_func():
    date_str = "2022-01-01"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    result = task_func(date_str, from_tz, to_tz)
    assert result == 1.0

def test_task_func_with_different_input():
    date_str = "2020-01-01"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    result = task_func(date_str, from_tz, to_tz)
    assert result == -1.0
import pytest
from src_1046 import task_func
from datetime import datetime
import numpy as np
from dateutil.parser import parse
LEAP_SECONDS = np.array(
    [
        1972,
        1973,
        1974,
        1975,
        1976,
        1977,
        1978,
        1979,
        1980,
        1981,
        1982,
        1983,
        1985,
        1988,
        1990,
        1993,
        1994,
        1997,
        1999,
        2006,
        2009,
        2012,
        2015,
        2016,
        2020,
    ]
)

def test_task_func():
    given_date = datetime(2022, 1, 1)
    current_date = datetime.now()
    total_seconds = (current_date - given_date).total_seconds()
    leap_seconds = np.sum(LEAP_SECONDS >= given_date.year)
    total_seconds += leap_seconds
    expected_result = int(total_seconds)
    actual_result = task_func("2022-01-01")
    assert actual_result == expected_result

def test_task_func_with_leap_seconds():
    given_date = datetime(2022, 6, 30, 23, 59, 60)
    current_date = datetime.now()
    total_seconds = (current_date - given_date).total_seconds()
    leap_seconds = np.sum(LEAP_SECONDS >= given_date.year)
    total_seconds += leap_seconds
    expected_result = int(total_seconds)
    actual_result = task_func("2022-06-30T23:59:60")
    assert actual_result == expected_result

def test_task_func_with_zero_seconds():
    given_date = datetime(2022, 1, 1)
    current_date = datetime.now()
    total_seconds = (current_date - given_date).total_seconds()
    leap_seconds = np.sum(LEAP_SECONDS >= given_date.year)
    total_seconds += leap_seconds
    expected_result = int(total_seconds)
    actual_result = task_func("2022-01-01")
    assert actual_result == expected_result

def test_task_func_with_negative_seconds():
    given_date = datetime(2022, 1, 1)
    current_date = datetime.now()
    total_seconds = (current_date - given_date).total_seconds()
    leap_seconds = np.sum(LEAP_SECONDS >= given_date.year)
    total_seconds += leap_seconds
    expected_result = int(total_seconds)
    actual_result = task_func("2022-01-01")
    assert actual_result == expected_result
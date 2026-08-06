import pytest
from src_0650 import task_func
import numpy as np
import pandas as pd
from dateutil.parser import parse

def test_task_func():
    # Test with a list of dates covering all days of the week
    dates_str_list = [
        "2023-10-02",  # Monday
        "2023-10-03",  # Tuesday
        "2023-10-04",  # Wednesday
        "2023-10-05",  # Thursday
        "2023-10-06",  # Friday
        "2023-10-07",  # Saturday
        "2023-10-08"   # Sunday
    ]
    expected_output = pd.Series([1, 1, 1, 1, 1, 1, 1], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_output)

    # Test with an empty list
    dates_str_list = []
    expected_output = pd.Series([0, 0, 0, 0, 0, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_output)

    # Test with multiple occurrences of the same day
    dates_str_list = [
        "2023-10-02",  # Monday
        "2023-10-02",  # Monday
        "2023-10-02",  # Monday
        "2023-10-03",  # Tuesday
        "2023-10-03"   # Tuesday
    ]
    expected_output = pd.Series([3, 2, 0, 0, 0, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_output)

    # Test with different formats of date strings
    dates_str_list = [
        "02/10/2023",  # Monday
        "2023-10-03",  # Tuesday
        "10/04/2023",  # Wednesday
        "2023.10.05",  # Thursday
        "2023/10/06",  # Friday
        "10-07-2023",  # Saturday
        "2023 10 08"   # Sunday
    ]
    expected_output = pd.Series([1, 1, 1, 1, 1, 1, 1], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_output)

    # Test with invalid date string
    dates_str_list = ["not-a-date"]
    with pytest.raises(ValueError):
        task_func(dates_str_list)
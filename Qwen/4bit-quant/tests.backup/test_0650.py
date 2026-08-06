import pytest
from src_0650 import task_func
import numpy as np
import pandas as pd
from dateutil.parser import parse

def test_task_func():
    # Test with a list of dates that cover all days of the week
    dates_str_list = ["2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", "2023-10-06", "2023-10-07", "2023-10-08"]
    expected_output = pd.Series([0, 1, 1, 1, 1, 1, 1], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_output)

    # Test with an empty list
    dates_str_list = []
    expected_output = pd.Series([0, 0, 0, 0, 0, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_output)

    # Test with a list of dates that have multiple occurrences of the same day
    dates_str_list = ["2023-10-02", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-04", "2023-10-04"]
    expected_output = pd.Series([2, 1, 1, 0, 0, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_output)

    # Test with a list of dates that include only weekends
    dates_str_list = ["2023-10-07", "2023-10-08", "2023-10-14", "2023-10-15"]
    expected_output = pd.Series([0, 0, 0, 0, 0, 2, 2], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_output)

    # Test with a list of dates that include only weekdays
    dates_str_list = ["2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05", "2023-10-06"]
    expected_output = pd.Series([1, 1, 1, 1, 1, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_output)
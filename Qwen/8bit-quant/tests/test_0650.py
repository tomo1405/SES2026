import pandas as pd
import pytest
from src_0650 import task_func


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
    expected_distribution = pd.Series([1, 1, 1, 1, 1, 1, 1], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_distribution)

    # Test with multiple occurrences of the same day
    dates_str_list = [
        "2023-10-02",  # Monday
        "2023-10-02",  # Monday
        "2023-10-03",  # Tuesday
        "2023-10-03",  # Tuesday
        "2023-10-04",  # Wednesday
        "2023-10-05",  # Thursday
        "2023-10-06",  # Friday
        "2023-10-07",  # Saturday
        "2023-10-08"   # Sunday
    ]
    expected_distribution = pd.Series([2, 2, 1, 1, 1, 1, 1], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_distribution)

    # Test with an empty list
    dates_str_list = []
    expected_distribution = pd.Series([0, 0, 0, 0, 0, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_distribution)

    # Test with a single date
    dates_str_list = ["2023-10-02"]  # Monday
    expected_distribution = pd.Series([1, 0, 0, 0, 0, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_distribution)

    # Test with invalid date strings
    dates_str_list = ["2023-10-32", "2023-02-29", "not-a-date"]
    with pytest.raises(ValueError):
        task_func(dates_str_list)
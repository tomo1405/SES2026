import pytest
import numpy as np
import pandas as pd
from dateutil.parser import parse
from src_0650 import task_func

def test_task_func():
    dates_str_list = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
    expected_distribution = pd.Series([1, 1, 1, 1, 1, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    result = task_func(dates_str_list)
    assert result.equals(expected_distribution)

def test_task_func_with_empty_list():
    dates_str_list = []
    expected_distribution = pd.Series([0, 0, 0, 0, 0, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    result = task_func(dates_str_list)
    assert result.equals(expected_distribution)

def test_task_func_with_one_date_str():
    dates_str_list = ['2023-01-01']
    expected_distribution = pd.Series([0, 0, 0, 0, 0, 0, 1], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    result = task_func(dates_str_list)
    assert result.equals(expected_distribution)

def test_task_func_with_invalid_date_str():
    dates_str_list = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
    with pytest.raises(ValueError):
        task_func(dates_str_list)
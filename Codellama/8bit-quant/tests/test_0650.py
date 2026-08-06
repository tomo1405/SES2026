import pytest
from src_0650 import task_func
import numpy as np
import pandas as pd
from dateutil.parser import parse

def test_task_func():
    dates_str_list = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07']
    expected_distribution = pd.Series([1, 1, 1, 1, 1, 1, 1], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_distribution)

def test_task_func_with_invalid_input():
    dates_str_list = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08']
    with pytest.raises(ValueError):
        task_func(dates_str_list)
import pandas as pd
import pytest
from src_0650 import task_func


def test_task_func():
    dates_str_list = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05']
    expected_distribution = pd.Series([1, 1, 1, 1, 1], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
    assert task_func(dates_str_list).equals(expected_distribution)

def test_task_func_with_invalid_input():
    dates_str_list = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05']
    with pytest.raises(ValueError):
        task_func(dates_str_list, invalid_input=True)
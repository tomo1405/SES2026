python
import pytest
from src_0650 import task_func

def test_task_func():
    dates_str_list = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07']
    expected_distribution = pd.Series([1, 1, 1, 1, 1, 1, 1], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    assert task_func(dates_str_list).equals(expected_distribution)
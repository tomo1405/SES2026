import pytest
from src_0650 import task_func

def test_task_func():
    dates_str_list = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
    expected_distribution = pd.Series([1, 1, 1, 1, 1, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    actual_distribution = task_func(dates_str_list)
    
    assert actual_distribution.equals(expected_distribution)
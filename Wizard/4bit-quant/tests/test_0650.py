python
import pytest
from src_0650 import task_func

def test_task_func():
    dates_str_list = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07']
    expected_distribution = pd.Series([0, 0, 0, 0, 0, 0, 0], index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    expected_distribution['Monday'] = 1
    expected_distribution['Tuesday'] = 1
    expected_distribution['Wednesday'] = 1
    expected_distribution['Thursday'] = 1
    expected_distribution['Friday'] = 1
    expected_distribution['Saturday'] = 1
    expected_distribution['Sunday'] = 1
    
    distribution = task_func(dates_str_list)
    
    assert distribution.equals(expected_distribution)
python
import pytest
from src_0627 import task_func

def test_task_func():
    # Test case 1
    date_str = '2022-01-01 12:00:00'
    from_tz = 'Asia/Tokyo'
    expected_result = ('2022-01-01 15:00:00', 'Asia/Tokyo')
    assert task_func(date_str, from_tz) == expected_result

    # Test case 2
    date_str = '2022-07-01 12:00:00'
    from_tz = 'Europe/London'
    expected_result = ('2022-07-01 13:00:00', 'Europe/London')
    assert task_func(date_str, from_tz) == expected_result

    # Test case 3
    date_str = '2022-12-31 23:59:59'
    from_tz = 'America/New_York'
    expected_result = ('2023-01-01 03:59:59', 'America/New_York')
    assert task_func(date_str, from_tz) == expected_result

    # Test case 4
    date_str = '2022-01-01 12:00:00'
    from_tz = 'Australia/Sydney'
    expected_result = ('2022-01-01 15:00:00', 'Australia/Sydney')
    assert task_func(date_str, from_tz) == expected_result

    # Test case 5
    date_str = '2022-01-01 12:00:00'
    from_tz = 'Asia/Shanghai'
    expected_result = ('2022-01-01 15:00:00', 'Asia/Shanghai')
    assert task_func(date_str, from_tz) == expected_result
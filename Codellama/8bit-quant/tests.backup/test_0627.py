import pytest
from src_0627 import task_func

def test_task_func():
    date_str = '2022-01-01 12:00:00'
    from_tz = 'America/New_York'
    expected_date = '2022-01-01 17:00:00'
    expected_tz = 'Asia/Shanghai'

    assert task_func(date_str, from_tz) == (expected_date, expected_tz)

def test_task_func_with_different_timezone():
    date_str = '2022-01-01 12:00:00'
    from_tz = 'Europe/London'
    expected_date = '2022-01-01 13:00:00'
    expected_tz = 'Asia/Tokyo'

    assert task_func(date_str, from_tz) == (expected_date, expected_tz)

def test_task_func_with_invalid_timezone():
    date_str = '2022-01-01 12:00:00'
    from_tz = 'Invalid/Timezone'

    with pytest.raises(ValueError):
        task_func(date_str, from_tz)
import pytest
from src_0495 import task_func

def test_task_func():
    # Test case 1: epoch_milliseconds = 1632345600000, seed = 0, timezones = ["UTC"]
    expected_output = {
        'John': [
            {
                'date': datetime.date(2021, 9, 24),
                'time': datetime.time(12, 0),
                'timezone': 'UTC'
            }
        ]
    }
    assert task_func(1632345600000, 0, ["UTC"]) == expected_output

    # Test case 2: epoch_milliseconds = 1632345600000, seed = 0, timezones = ["UTC", "America/New_York"]
    expected_output = {
        'John': [
            {
                'date': datetime.date(2021, 9, 24),
                'time': datetime.time(20, 0),
                'timezone': 'America/New_York'
            }
        ]
    }
    assert task_func(1632345600000, 0, ["UTC", "America/New_York"]) == expected_output

    # Test case 3: epoch_milliseconds = 1632345600000, seed = 0, timezones = ["UTC", "America/New_York", "Asia/Tokyo"]
    expected_output = {
        'John': [
            {
                'date': datetime.date(2021, 9, 24),
                'time': datetime.time(22, 0),
                'timezone': 'Asia/Tokyo'
            }
        ]
    }
    assert task_func(1632345600000, 0, ["UTC", "America/New_York", "Asia/Tokyo"]) == expected_output
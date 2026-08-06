import pytest
from src_1075 import task_func
import pytz
from dateutil.parser import parse

def test_task_func():
    # Test case 1: Normal case
    time_string = "15/10/20 13:45:30.123"
    from_tz = "UTC"
    to_tz = "US/Eastern"
    expected_output = "10/15/20 09:45:30.123"
    assert task_func(time_string, from_tz, to_tz) == expected_output

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()
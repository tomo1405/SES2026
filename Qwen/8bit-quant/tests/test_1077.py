import pytest
from src_1077 import task_func
from datetime import datetime
import pandas as pd

def test_task_func_with_valid_input():
    time_strings = ["01/01/22 12:00:00.000000", "02/01/22 13:00:00.000000"]
    target_tz = "America/New_York"
    expected_output = pd.DataFrame({
        "Original Time": ["01/01/22 12:00:00.000000", "02/01/22 13:00:00.000000"],
        "Converted Time": [
            "01/01/22 07:00:00.000000",  # Example conversion, actual value may vary
            "02/01/22 08:00:00.000000"   # Example conversion, actual value may vary
        ]
    })
    result_df = task_func(time_strings, target_tz)
    assert result_df.equals(expected_output)

def test_task_func_with_empty_input():
    time_strings = []
    target_tz = "Europe/London"
    expected_output = pd.DataFrame(columns=["Original Time", "Converted Time"])
    result_df = task_func(time_strings, target_tz)
    assert result_df.equals(expected_output)

def test_task_func_with_single_time_string():
    time_strings = ["01/01/22 12:00:00.000000"]
    target_tz = "Asia/Tokyo"
    expected_output = pd.DataFrame({
        "Original Time": ["01/01/22 12:00:00.000000"],
        "Converted Time": [
            "02/01/22 09:00:00.000000"  # Example conversion, actual value may vary
        ]
    })
    result_df = task_func(time_strings, target_tz)
    assert result_df.equals(expected_output)

def test_task_func_with_invalid_time_format():
    time_strings = ["01-01-22 12:00:00.000000"]  # Invalid format
    target_tz = "Europe/Berlin"
    with pytest.raises(ValueError):
        task_func(time_strings, target_tz)

def test_task_func_with_invalid_timezone():
    time_strings = ["01/01/22 12:00:00.000000"]
    target_tz = "Invalid/Timezone"
    with pytest.raises(Exception):
        task_func(time_strings, target_tz)
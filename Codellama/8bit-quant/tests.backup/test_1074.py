import pytest
from src_1074 import task_func

def test_task_func_valid_input():
    time_strings = ["12/01/2023 12:34:56.789", "13/01/2023 13:45:06.890"]
    time_format = "%d/%m/%Y %H:%M:%S.%f"
    ax = task_func(time_strings, time_format)
    assert ax is not None
    assert ax.get_title() == "Histogram of seconds"
    assert ax.get_xlabel() == "Seconds"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xlim() == (0, 60)
    assert ax.get_ylim() == (0, 2)
    assert ax.get_xticks() == [0, 10, 20, 30, 40, 50]
    assert ax.get_yticks() == [0, 1, 2]
    assert ax.get_xticklabels() == ["00", "10", "20", "30", "40", "50"]
    assert ax.get_yticklabels() == ["0", "1", "2"]

def test_task_func_invalid_input():
    time_strings = ["12/01/2023 12:34:56.789", "13/01/2023 13:45:06.890", "invalid"]
    time_format = "%d/%m/%Y %H:%M:%S.%f"
    ax = task_func(time_strings, time_format)
    assert ax is None
    assert "Error parsing time strings: time data 'invalid' does not match format '%d/%m/%Y %H:%M:%S.%f'" in caplog.text
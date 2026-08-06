import pytest
from src_1074 import task_func

def test_task_func_valid_input():
    time_strings = ["12/01/2023 12:00:00.000", "12/01/2023 12:00:01.000", "12/01/2023 12:00:02.000"]
    time_format = "%d/%m/%Y %H:%M:%S.%f"
    ax = task_func(time_strings, time_format)
    assert ax is not None
    assert ax.get_title() == "Histogram of seconds"
    assert ax.get_xlabel() == "Seconds"
    assert ax.get_ylabel() == "Count"
    assert ax.get_xlim() == (0, 60)
    assert ax.get_ylim() == (0, 3)
    assert ax.get_xticks() == [0, 10, 20, 30, 40, 50]
    assert ax.get_yticks() == [0, 1, 2, 3]

def test_task_func_invalid_input():
    time_strings = ["12/01/2023 12:00:00.000", "12/01/2023 12:00:01.000", "12/01/2023 12:00:02.000"]
    time_format = "%d/%m/%Y %H:%M:%S.%f"
    ax = task_func(time_strings, time_format)
    assert ax is None
    assert "Error parsing time strings" in caplog.text
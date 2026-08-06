import pytest
from src_1074 import task_func

def test_task_func():
    time_strings = ["01/01/2023 12:00:00.000000", "01/01/2023 12:00:01.000000"]
    ax = task_func(time_strings)
    assert ax is not None
    assert ax.get_xlabel() == "Second"
    assert ax.get_ylabel() == "Frequency"

def test_task_func_with_invalid_time_strings():
    time_strings = ["01/01/2023 12:00:00.000000", "invalid_time_string"]
    ax = task_func(time_strings)
    assert ax is None
    assert "Error parsing time strings" in capsys.readouterr().err
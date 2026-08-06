import pytest
from src_1029 import task_func


def test_task_func_valid_input():
    interval = 1
    duration = 5
    result = task_func(interval, duration)
    assert result == "logfile.log"

def test_task_func_invalid_input():
    interval = 0
    duration = 0
    with pytest.raises(ValueError) as excinfo:
        task_func(interval, duration)
    assert "Interval and duration must be greater than zero." in str(excinfo.value)

def test_task_func_ioerror():
    interval = 1
    duration = 5
    with mock.patch("src_1029.open", side_effect=IOError("Test error")):
        result = task_func(interval, duration)
    assert result is None
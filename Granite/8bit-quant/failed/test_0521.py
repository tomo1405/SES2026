import pytest
from src_0521 import task_func

def test_task_func():
    data = [
        {"apple": 10, "banana": 5},
        {"apple": 8, "banana": 12, "orange": 3},
        {"apple": 5, "orange": 7}
    ]
    expected_output = (
        {"apple": 23, "banana": 17, "orange": 10},
        None
    )
    actual_output = task_func(data)
    assert actual_output == expected_output, "Task function returned incorrect output"

def test_task_func_with_negative_value():
    data = [
        {"apple": 10, "banana": 5},
        {"apple": 8, "banana": 12, "orange": -3},
        {"apple": 5, "orange": 7}
    ]
    with pytest.raises(ValueError) as exc_info:
        task_func(data)
    assert "Sales quantity must not be negative." in str(exc_info.value), "Task function did not raise expected ValueError"
import pytest
from src_0521 import task_func

def test_task_func():
    data = [
        {"apple": 10, "banana": 5},
        {"apple": 8, "banana": 3, "orange": 2},
        {"apple": 12, "orange": 5}
    ]
    expected_output = (
        {"apple": 20, "banana": 8, "orange": 7},
        None
    )
    actual_output = task_func(data)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_negative_value():
    data = [
        {"apple": 10, "banana": 5},
        {"apple": 8, "banana": -3, "orange": 2},
        {"apple": 12, "orange": 5}
    ]
    with pytest.raises(ValueError) as exc_info:
        task_func(data)
    assert "Sales quantity must not be negative." in str(exc_info.value), "Expected ValueError not raised"
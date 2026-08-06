import pytest
from src_0521 import task_func

def test_task_func():
    data = [
        {"apple": 10, "banana": 5},
        {"apple": 8, "orange": 12},
        {"apple": 5, "banana": 3, "orange": 2}
    ]
    expected_output = (
        {"apple": 23, "banana": 8, "orange": 14},
        pytest.approx([23, 8, 14])
    )
    actual_output = task_func(data)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_negative_values():
    data = [
        {"apple": 10, "banana": -5},
        {"apple": 8, "orange": 12},
        {"apple": 5, "banana": 3, "orange": 2}
    ]
    with pytest.raises(ValueError) as exc_info:
        task_func(data)
    assert "Sales quantity must not be negative." in str(exc_info.value)
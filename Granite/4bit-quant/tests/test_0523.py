import pytest
from src_0523 import task_func

def test_task_func():
    data = [
        {"Alice": 85, "Bob": 92, "Charlie": 78},
        {"Alice": 95, "Bob": 88, "Charlie": 92},
        {"Alice": 75, "Bob": 82, "Charlie": 68},
        {"Alice": 90, "Bob": 92, "Charlie": 88}
    ]
    expected_output = "bar plot"

    ax = task_func(data)
    assert ax == expected_output, "Output does not match expected output"

def test_task_func_with_empty_data():
    data = []
    expected_output = None

    ax = task_func(data)
    assert ax == expected_output, "Output does not match expected output"

def test_task_func_with_negative_scores():
    data = [
        {"Alice": 85, "Bob": -2, "Charlie": 78},
        {"Alice": 95, "Bob": 88, "Charlie": 92},
        {"Alice": 75, "Bob": 82, "Charlie": 68},
        {"Alice": 90, "Bob": 92, "Charlie": 88}
    ]

    with pytest.raises(ValueError) as exc_info:
        task_func(data)
    assert "Scores must be non-negative." in str(exc_info.value), "Expected ValueError not raised"
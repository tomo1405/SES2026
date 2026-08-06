import pytest
from src_0523 import task_func

def test_task_func():
    data = [
        {"Alice": 85, "Bob": 92, "Charlie": 78},
        {"Alice": 95, "Bob": 88, "Charlie": 92},
        {"Alice": 75, "Bob": 82, "Charlie": 88},
        {"Alice": 90, "Bob": 92, "Charlie": 85}
    ]
    expected_output = "bar plot object"
    actual_output = task_func(data)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_empty_data():
    data = []
    expected_output = None
    actual_output = task_func(data)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_negative_scores():
    data = [
        {"Alice": 85, "Bob": 92, "Charlie": -2},
        {"Alice": 95, "Bob": 88, "Charlie": 92},
        {"Alice": 75, "Bob": 82, "Charlie": 88},
        {"Alice": 90, "Bob": 92, "Charlie": 85}
    ]
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert "Scores must be non-negative." in str(excinfo.value), "Expected error message not raised"
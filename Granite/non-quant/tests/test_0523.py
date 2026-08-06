import pytest
from src_0523 import task_func

def test_task_func():
    data = [
        {"A": 10, "B": 20, "C": 30},
        {"A": 15, "B": 25, "C": 35},
        {"A": 20, "B": 30, "C": 40},
        {"A": 25, "B": 35, "C": 45},
        {"A": 30, "B": 40, "C": 50},
    ]
    expected_output = "bar chart object"
    actual_output = task_func(data)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_empty_data():
    data = []
    expected_output = None
    actual_output = task_func(data)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_negative_score():
    data = [
        {"A": 10, "B": 20, "C": 30},
        {"A": 15, "B": 25, "C": 35},
        {"A": 20, "B": 30, "C": -40},
        {"A": 25, "B": 35, "C": 45},
        {"A": 30, "B": 40, "C": 50},
    ]
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert "Scores must be non-negative." in str(excinfo.value), "Expected ValueError not raised"
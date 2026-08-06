import pytest
from src_1083 import task_func

def test_task_func_with_valid_data():
    data = [
        {"Score_String": "90", "Grade": "A"},
        {"Score_String": "80", "Grade": "B"},
        {"Score_String": "70", "Grade": "C"},
        {"Score_String": "60", "Grade": "D"},
        {"Score_String": "50", "Grade": "F"}
    ]
    expected_correlation = 0.8
    actual_correlation = task_func(data)
    assert actual_correlation == expected_correlation

def test_task_func_with_invalid_data():
    data = [
        {"Score_String": "90", "Grade": "A"},
        {"Score_String": "80", "Grade": "B"},
        {"Score_String": "70", "Grade": "C"},
        {"Score_String": "60", "Grade": "D"},
        {"Score_String": "50", "Grade": "F"}
    ]
    expected_correlation = float("nan")
    actual_correlation = task_func(data)
    assert actual_correlation == expected_correlation

def test_task_func_with_empty_data():
    data = []
    expected_correlation = float("nan")
    actual_correlation = task_func(data)
    assert actual_correlation == expected_correlation
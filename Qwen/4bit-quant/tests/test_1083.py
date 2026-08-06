import pytest
from src_1083 import task_func

def test_task_func_with_valid_data():
    data = {
        "Score_String": ["85.5", "90.0", "78.2"],
        "Grade": ["A", "B", "C"]
    }
    result = task_func(data)
    assert isinstance(result, float)

def test_task_func_with_less_than_two_rows():
    data = {
        "Score_String": ["85.5"],
        "Grade": ["A"]
    }
    result = task_func(data)
    assert result == float("nan")

def test_task_func_with_non_numeric_score():
    data = {
        "Score_String": ["eighty-five", "ninety"],
        "Grade": ["A", "B"]
    }
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_with_empty_data():
    data = {}
    result = task_func(data)
    assert result == float("nan")

def test_task_func_with_all_null_scores():
    data = {
        "Score_String": [None, None],
        "Grade": ["A", "B"]
    }
    result = task_func(data)
    assert result == float("nan")

def test_task_func_with_all_null_grades():
    data = {
        "Score_String": ["85.5", "90.0"],
        "Grade": [None, None]
    }
    result = task_func(data)
    assert result == float("nan")
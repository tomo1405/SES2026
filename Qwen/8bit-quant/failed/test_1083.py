import pytest
from src_1083 import task_func
import pandas as pd
import numpy as np

def test_task_func_with_valid_data():
    data = {
        "Score_String": ["85", "90", "78", "92"],
        "Grade": ["A", "B", "C", "A"]
    }
    expected_correlation = 0.816496580927726  # This is an approximate value
    assert np.isclose(task_func(data), expected_correlation, atol=1e-6)

def test_task_func_with_single_row():
    data = {
        "Score_String": ["85"],
        "Grade": ["A"]
    }
    assert np.isnan(task_func(data))

def test_task_func_with_empty_data():
    data = {}
    assert np.isnan(task_func(data))

def test_task_func_with_non_numeric_score():
    data = {
        "Score_String": ["85", "abc", "78", "92"],
        "Grade": ["A", "B", "C", "A"]
    }
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_with_non_categorical_grade():
    data = {
        "Score_String": ["85", "90", "78", "92"],
        "Grade": [1, 2, 3, 1]
    }
    expected_correlation = 0.816496580927726  # This is an approximate value
    assert np.isclose(task_func(data), expected_correlation, atol=1e-6)
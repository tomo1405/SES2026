import pytest
from src_1083 import task_func
import pandas as pd
from scipy.stats import pearsonr

def test_task_func_with_valid_data():
    data = {
        "Score_String": ["90", "85", "78", "92"],
        "Grade": ["A", "B", "C", "A"]
    }
    result = task_func(data)
    assert isinstance(result, float)

def test_task_func_with_less_than_two_rows():
    data = {
        "Score_String": ["90"],
        "Grade": ["A"]
    }
    result = task_func(data)
    assert pd.isna(result)

def test_task_func_with_non_numeric_score():
    data = {
        "Score_String": ["90", "invalid", "78", "92"],
        "Grade": ["A", "B", "C", "A"]
    }
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_with_empty_data():
    data = {
        "Score_String": [],
        "Grade": []
    }
    result = task_func(data)
    assert pd.isna(result)

def test_task_func_with_single_unique_grade():
    data = {
        "Score_String": ["90", "85", "78", "92"],
        "Grade": ["A", "A", "A", "A"]
    }
    result = task_func(data)
    assert result == 0.0

def test_task_func_with_perfect_correlation():
    data = {
        "Score_String": ["90", "85", "78", "92"],
        "Grade": ["A", "B", "C", "D"]
    }
    expected_correlation = pearsonr([90, 85, 78, 92], [0, 1, 2, 3])[0]
    result = task_func(data)
    assert abs(result - expected_correlation) < 1e-6
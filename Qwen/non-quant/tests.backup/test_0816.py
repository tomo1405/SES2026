import pytest
from src_0816 import task_func
import pandas as pd
import numpy as np

def test_task_func_student_not_present():
    test_scores = [
        {'Student': 'Alice', 'Score': 85},
        {'Student': 'Bob', 'Score': 90}
    ]
    student = 'Charlie'
    with pytest.raises(ValueError) as excinfo:
        task_func(test_scores, student)
    assert str(excinfo.value) == f"The student with ID {student} is not present in the test scores DataFrame."

def test_task_func_valid_student():
    test_scores = [
        {'Student': 'Alice', 'Score': 85},
        {'Student': 'Alice', 'Score': 90},
        {'Student': 'Bob', 'Score': 92}
    ]
    student = 'Alice'
    expected_average = (85 + 90) / 2
    expected_std = np.std([85, 90])
    result, df = task_func(test_scores, student)
    assert np.isclose(result[0], expected_average)
    assert np.isclose(result[1], expected_std)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3

def test_task_func_single_score():
    test_scores = [
        {'Student': 'Alice', 'Score': 85}
    ]
    student = 'Alice'
    expected_average = 85
    expected_std = 0
    result, df = task_func(test_scores, student)
    assert np.isclose(result[0], expected_average)
    assert np.isclose(result[1], expected_std)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
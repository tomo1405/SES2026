import pytest
from src_0816 import task_func
import pandas as pd
import numpy as np

# Mock data for testing
test_scores_data = {
    'Student': ['A', 'B', 'C'],
    'Score': [85, 92, 78]
}

def test_task_func_valid_student():
    student = 'B'
    expected_average = 92.0
    expected_std = 0.0
    result, df = task_func(test_scores_data, student)
    assert np.isclose(result[0], expected_average)
    assert np.isclose(result[1], expected_std)
    assert isinstance(df, pd.DataFrame)

def test_task_func_invalid_student():
    student = 'D'
    with pytest.raises(ValueError) as excinfo:
        task_func(test_scores_data, student)
    assert str(excinfo.value) == f"The student with ID {student} is not present in the test scores DataFrame."

def test_task_func_single_student():
    student = 'C'
    expected_average = 78.0
    expected_std = 0.0
    result, df = task_func(test_scores_data, student)
    assert np.isclose(result[0], expected_average)
    assert np.isclose(result[1], expected_std)
    assert isinstance(df, pd.DataFrame)

def test_task_func_multiple_students_same_score():
    test_scores_data = {
        'Student': ['A', 'A', 'B'],
        'Score': [85, 85, 92]
    }
    student = 'A'
    expected_average = 85.0
    expected_std = 0.0
    result, df = task_func(test_scores_data, student)
    assert np.isclose(result[0], expected_average)
    assert np.isclose(result[1], expected_std)
    assert isinstance(df, pd.DataFrame)
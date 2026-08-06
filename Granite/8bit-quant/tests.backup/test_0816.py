import pandas as pd
import numpy as np
from src_0816 import task_func
import pytest

def test_task_func():
    test_scores = pd.DataFrame({
        'Student': ['A', 'B', 'C', 'D'],
        'Score': [80, 90, 75, 95]
    })
    student = 'A'
    expected_output = (np.array([80, 0]), test_scores)
    actual_output = task_func(test_scores, student)
    assert np.array_equal(actual_output[0], expected_output[0]) and actual_output[1].equals(expected_output[1])

def test_task_func_with_invalid_student():
    test_scores = pd.DataFrame({
        'Student': ['A', 'B', 'C', 'D'],
        'Score': [80, 90, 75, 95]
    })
    student = 'E'
    with pytest.raises(ValueError) as exc_info:
        task_func(test_scores, student)
    assert str(exc_info.value) == "The student with ID E is not present in the test scores DataFrame."
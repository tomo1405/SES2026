import numpy as np
import pandas as pd
import pytest
from src_0816 import task_func


def test_task_func():
    test_scores = pd.DataFrame({'Student': ['A', 'B', 'C'], 'Score': [90, 80, 70]})
    student = 'A'
    expected_output = np.array([90, 10])
    actual_output, test_scores = task_func(test_scores, student)
    assert np.array_equal(actual_output, expected_output)

def test_task_func_invalid_student():
    test_scores = pd.DataFrame({'Student': ['A', 'B', 'C'], 'Score': [90, 80, 70]})
    student = 'D'
    with pytest.raises(ValueError):
        task_func(test_scores, student)
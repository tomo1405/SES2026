import pandas as pd
import pytest
from src_0816 import task_func


def test_task_func():
    test_scores = pd.DataFrame({'Student': [1, 2, 3], 'Score': [90, 80, 70]})
    student = 1
    expected_average_score = 90
    expected_std = 0
    expected_test_scores = pd.DataFrame({'Student': [1, 2, 3], 'Score': [90, 80, 70]})
    actual_result, actual_test_scores = task_func(test_scores, student)
    assert actual_result[0] == expected_average_score
    assert actual_result[1] == expected_std
    assert actual_test_scores.equals(expected_test_scores)

def test_task_func_invalid_student():
    test_scores = pd.DataFrame({'Student': [1, 2, 3], 'Score': [90, 80, 70]})
    student = 4
    with pytest.raises(ValueError):
        task_func(test_scores, student)
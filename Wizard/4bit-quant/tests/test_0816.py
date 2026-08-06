python
import pandas as pd
import numpy as np
import pytest

def task_func(test_scores, student):
    test_scores = pd.DataFrame(test_scores)
    if student not in test_scores['Student'].values:
        raise ValueError(f"The student with ID {student} is not present in the test scores DataFrame.")
    student_scores = test_scores[test_scores['Student'] == student]['Score']
    average_score = student_scores.mean()
    std = student_scores.std()
    
    return np.array([average_score, std]), test_scores

def test_task_func():
    test_scores = {'Student': ['A', 'B', 'C', 'D'], 'Score': [80, 70, 90, 60]}
    student = 'B'
    expected_result = np.array([70, 10.0])
    
    result, test_scores = task_func(test_scores, student)
    
    assert np.array_equal(result, expected_result)
    assert isinstance(test_scores, pd.DataFrame)
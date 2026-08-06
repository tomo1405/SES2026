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
    test_scores = {'Student': ['A', 'B', 'C'], 'Score': [80, 70, 90]}
    student = 'B'
    expected_result = np.array([70, 10]), pd.DataFrame({'Student': ['A', 'B', 'C'], 'Score': [80, 70, 90]})
    
    result = task_func(test_scores, student)
    
    assert result[0].all() == expected_result[0].all()
    assert result[1].equals(expected_result[1])
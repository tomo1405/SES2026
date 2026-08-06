import pandas as pd
import numpy as np
import pytest

from src_0816 import task_func

def test_task_func():
    test_scores = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    student = 2
    expected_output = (np.array([5, 1]), pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    actual_output = task_func(test_scores, student)
    assert actual_output == expected_output, "Output does not match expected output"

def test_task_func_with_invalid_student_id():
    test_scores = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    student = 4
    with pytest.raises(ValueError) as e:
        task_func(test_scores, student)
    assert "The student with ID 4 is not present in the test scores DataFrame." in str(e.value), "Invalid student ID error message not raised"
python
import pandas as pd
import pytest
from scipy.stats import pearsonr
from src_1083 import task_func

def test_task_func():
    # Test case 1: Test with valid data
    data = {"Score_String": ["90", "80", "70"], "Grade": ["A", "B", "C"]}
    expected_result = 0.9999999999999999
    result = task_func(data)
    assert result == expected_result

    # Test case 2: Test with invalid data (less than 2 rows)
    data = {"Score_String": ["90"], "Grade": ["A"]}
    expected_result = float("nan")
    result = task_func(data)
    assert result == expected_result

    # Test case 3: Test with invalid data (non-numeric score)
    data = {"Score_String": ["90", "80", "A"], "Grade": ["A", "B", "C"]}
    expected_result = float("nan")
    result = task_func(data)
    assert result == expected_result

    # Test case 4: Test with invalid data (non-categorical grade)
    data = {"Score_String": ["90", "80", "70"], "Grade": ["A", "B", "D"]}
    expected_result = float("nan")
    result = task_func(data)
    assert result == expected_result
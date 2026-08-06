python
import pandas as pd
import pytest
from src_0830 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [80, 70, 90]})
    expected_result = {'Alice': [('Alice', 80.0)], 'Bob': [('Bob', 70.0)], 'Charlie': [('Charlie', 90.0)]}
    assert task_func(df) == expected_result

    # Test case 2: Missing columns
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: Empty dataframe
    df = pd.DataFrame({'Name': [], 'Score': []})
    with pytest.raises(ValueError):
        task_func(df)
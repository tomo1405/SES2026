python
import pandas as pd
import pytest
from src_0372 import task_func

def test_task_func():
    # Test case 1
    l = [1, 2, 3, 4, 5]
    expected_df = pd.DataFrame([[0.0], [0.5], [1.0], [1.0], [1.0]], columns=['Scaled Values'])
    actual_df = task_func(l)
    assert actual_df.equals(expected_df)

    # Test case 2
    l = [5, 4, 3, 2, 1]
    expected_df = pd.DataFrame([[1.0], [1.0], [0.5], [0.0], [0.0]], columns=['Scaled Values'])
    actual_df = task_func(l)
    assert actual_df.equals(expected_df)

    # Test case 3
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_df = pd.DataFrame([[0.0], [0.2], [0.4], [0.6], [0.8], [1.0], [1.0], [1.0], [1.0], [1.0]], columns=['Scaled Values'])
    actual_df = task_func(l)
    assert actual_df.equals(expected_df)
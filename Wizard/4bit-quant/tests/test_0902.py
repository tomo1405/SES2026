python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0902 import task_func

def test_task_func():
    # Test case 1: Test with empty input list
    assert task_func([]) == pd.DataFrame(columns=['x', 'y', 'z'])

    # Test case 2: Test with non-empty input list
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = pd.DataFrame([[0.0, 0.0, 0.0], [0.5, 0.5, 0.5], [1.0, 1.0, 1.0]], columns=['x', 'y', 'z'])
    assert task_func(data).equals(expected_output)
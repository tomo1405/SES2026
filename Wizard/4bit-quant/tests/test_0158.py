python
import numpy as np
import pandas as pd
import seaborn as sns
import pytest

from src_0158 import task_func

def test_task_func():
    # Test case 1: Valid input data
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected_df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=[0, 1, 2])
    expected_ax = None
    actual_df, actual_ax = task_func(data)
    assert actual_df.equals(expected_df)
    assert actual_ax == expected_ax

    # Test case 2: Invalid input data (not a numpy array)
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(ValueError):
        task_func(data)

    # Test case 3: Invalid input data (not a 2D numpy array)
    data = np.array([1, 2, 3])
    with pytest.raises(ValueError):
        task_func(data)
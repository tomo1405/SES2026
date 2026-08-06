python
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0141 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    cols = ['A', 'B']
    expected_df = pd.DataFrame({'A': [-1.22474487, 0., 1.22474487], 'B': [-1.22474487, 0., 1.22474487]})
    assert task_func(df, cols).equals(expected_df)

    # Test case 2: Invalid input - df is not a DataFrame
    df = 'not a DataFrame'
    cols = ['A', 'B']
    with pytest.raises(ValueError):
        task_func(df, cols)

    # Test case 3: Invalid input - cols is not a list of strings
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    cols = ['A', 1]
    with pytest.raises(ValueError):
        task_func(df, cols)

    # Test case 4: Invalid input - cols contains a non-existent column
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    cols = ['A', 'C']
    with pytest.raises(ValueError):
        task_func(df, cols)
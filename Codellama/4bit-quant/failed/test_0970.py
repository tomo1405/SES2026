import pytest
from src_0970 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Test case 1: Input DataFrame contains non-numeric data types
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    with pytest.raises(TypeError):
        task_func(df)

    # Test case 2: Input DataFrame is empty
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: Input DataFrame contains NaN values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [np.nan, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 4: Input DataFrame is valid
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df_norm_cumsum = task_func(df)
    assert df_norm_cumsum.equals(pd.DataFrame({'A': [1, 3, 6], 'B': [4, 9, 15]}))
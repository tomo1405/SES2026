import numpy as np
import pandas as pd
import pytest
from src_0138 import task_func


def test_task_func():
    # Test 1: Input is not a DataFrame
    with pytest.raises(ValueError):
        task_func(1)

    # Test 2: Input is an empty DataFrame
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test 3: Input is a valid DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    skewness = task_func(df)
    assert isinstance(skewness, float)

    # Test 4: Input has NaN values
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, np.nan]})
    skewness = task_func(df)
    assert isinstance(skewness, float)

    # Test 5: Input has a different number of columns
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    skewness = task_func(df)
    assert isinstance(skewness, float)
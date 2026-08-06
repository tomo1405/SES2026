python
import numpy as np
import pandas as pd
import pytest
from src_0698 import task_func

def test_task_func():
    # Test case 1: Test with valid input data
    df = pd.DataFrame({'feature': [1, 2, 3], 'value': [4, 5, 6]})
    expected_output = {'coefficients': [4.0], 'intercept': [1.0]}
    assert task_func(df) == expected_output

    # Test case 2: Test with invalid input data (empty dataframe)
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: Test with invalid input data (missing feature column)
    df = pd.DataFrame({'value': [4, 5, 6]})
    with pytest.raises(KeyError):
        task_func(df)

    # Test case 4: Test with invalid input data (missing value column)
    df = pd.DataFrame({'feature': [1, 2, 3]})
    with pytest.raises(KeyError):
        task_func(df)

    # Test case 5: Test with invalid input data (non-numeric feature column)
    df = pd.DataFrame({'feature': ['a', 'b', 'c'], 'value': [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 6: Test with invalid input data (non-numeric value column)
    df = pd.DataFrame({'feature': [1, 2, 3], 'value': ['d', 'e', 'f']})
    with pytest.raises(ValueError):
        task_func(df)
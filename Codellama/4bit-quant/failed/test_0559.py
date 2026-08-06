import pytest
from src_0559 import task_func
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test with empty input lists
    df, ax = task_func([], [])
    assert df.empty
    assert ax.get_visible() == False

    # Test with non-empty input lists
    a = [1, 2, 3]
    b = [4, 5, 6]
    df, ax = task_func(a, b)
    assert df.equals(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}))
    assert ax.get_visible() == True

    # Test with custom column names
    df, ax = task_func(a, b, columns=['C', 'D'])
    assert df.equals(pd.DataFrame({'C': [1, 2, 3], 'D': [4, 5, 6]}))
    assert ax.get_visible() == True

    # Test with non-numeric input
    with pytest.raises(ValueError):
        task_func([1, 2, 3], ['a', 'b', 'c'])

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func([1, 2, 3], [4, 5, 6], columns=['A', 'B', 'C'])
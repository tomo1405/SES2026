import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_0135 import task_func

def test_task_func():
    # Test case 1: df is a non-empty pandas DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    ax = task_func(df)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test case 2: df is an empty pandas DataFrame
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: df is not a pandas DataFrame
    with pytest.raises(ValueError):
        task_func([1, 2, 3])
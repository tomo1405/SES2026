import matplotlib
import pandas as pd
import pytest
from src_0136 import task_func


def test_task_func():
    # Test 1: Input is not a DataFrame
    with pytest.raises(ValueError):
        task_func(1)

    # Test 2: Input is an empty DataFrame
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test 3: Input is a valid DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, ax = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (3, 2)
    assert ax.get_title() == 'Boxplot of Last Column'
    assert ax.get_xlabel() == 'B'
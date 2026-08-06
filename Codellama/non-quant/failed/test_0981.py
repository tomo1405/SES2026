import pytest
from src_0981 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    # Test case 1: No numeric columns present
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 2: Numeric columns present
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, fig = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Test case 3: Numeric columns present, but not all columns are numeric
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 4: Numeric columns present, but not all columns are numeric
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, fig = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Test case 5: Numeric columns present, but not all columns are numeric
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, fig = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Test case 6: Numeric columns present, but not all columns are numeric
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, fig = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Test case 7: Numeric columns present, but not all columns are numeric
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, fig = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Test case 8: Numeric columns present, but not all columns are numeric
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, fig = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Test case 9: Numeric columns present, but not all columns are numeric
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, fig = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Test case 10: Numeric columns present, but not all columns are numeric
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, fig = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)
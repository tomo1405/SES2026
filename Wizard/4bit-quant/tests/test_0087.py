python
import numpy as np
import pandas as pd
import pytest

from src_0087 import task_func

def test_task_func():
    students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    seed = 42

    # Test case 1: Test with default values
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)
    assert df.shape == (5, 2)
    assert df.columns.tolist() == ["Student", "Score"]
    assert df["Student"].tolist() == students
    assert df["Score"].min() >= 0
    assert df["Score"].max() <= 100

    # Test case 2: Test with custom values
    df, ax = task_func(students=students, seed=seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)
    assert df.shape == (5, 2)
    assert df.columns.tolist() == ["Student", "Score"]
    assert df["Student"].tolist() == students
    assert df["Score"].min() >= 0
    assert df["Score"].max() <= 100
import numpy as np
import pandas as pd
from src_0087 import task_func
import pytest

def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (5, 2)
    assert df.columns.tolist() == ["Student", "Score"]
    assert df["Student"].tolist() == ["Alice", "Bob", "Charlie", "David", "Eve"]
    assert df["Score"].dtype == np.int64
    assert ax.get_ylabel() == "Score"

def test_task_func_with_seed():
    df1, ax1 = task_func(seed=42)
    df2, ax2 = task_func(seed=42)
    assert df1.equals(df2)
    assert ax1.get_ylabel() == ax2.get_ylabel()

def test_task_func_with_students():
    df, ax = task_func(students=["Alice", "Bob", "Charlie"])
    assert df.shape == (3, 2)
    assert df["Student"].tolist() == ["Alice", "Bob", "Charlie"]
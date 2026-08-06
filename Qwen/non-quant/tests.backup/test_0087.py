import pytest
from src_0087 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_default():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (5, 2)
    assert list(df.columns) == ["Student", "Score"]
    assert df["Student"].tolist() == ["Alice", "Bob", "Charlie", "David", "Eve"]
    assert df["Score"].min() >= 0
    assert df["Score"].max() <= 100

def test_task_func_custom_students():
    students = ["John", "Jane", "Jack"]
    df, ax = task_func(students=students)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (3, 2)
    assert list(df.columns) == ["Student", "Score"]
    assert df["Student"].tolist() == students

def test_task_func_custom_seed():
    seed = 123
    df1, _ = task_func(seed=seed)
    df2, _ = task_func(seed=seed)
    assert df1.equals(df2)

def test_task_func_no_students():
    with pytest.raises(ValueError):
        task_func(students=[])

def test_task_func_invalid_seed_type():
    with pytest.raises(TypeError):
        task_func(seed="not_an_int")
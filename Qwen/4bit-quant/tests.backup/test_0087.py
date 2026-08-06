import pytest
from src_0087 import task_func
import numpy as np
import pandas as pd

def test_task_func_default():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, pd.plotting._matplotlib.bar.BarContainer)
    assert list(df.columns) == ["Student", "Score"]
    assert len(df) == 5
    assert all(isinstance(score, int) for score in df["Score"])

def test_task_func_custom_students():
    students = ["Tom", "Jerry", "Spike", "Tyke", "Butch"]
    df, ax = task_func(students=students)
    assert list(df["Student"]) == sorted(students)
    assert len(df) == len(students)

def test_task_func_custom_seed():
    seed = 99
    df1, _ = task_func(seed=seed)
    df2, _ = task_func(seed=seed)
    assert df1.equals(df2)

def test_task_func_empty_students():
    with pytest.raises(ValueError):
        task_func(students=[])

def test_task_func_single_student():
    df, ax = task_func(students=["OnlyOne"])
    assert len(df) == 1
    assert df.iloc[0]["Student"] == "OnlyOne"
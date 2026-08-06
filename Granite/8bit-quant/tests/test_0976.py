import numpy as np
import pandas as pd
from src_0976 import task_func
import pytest

def test_task_func_default_args():
    """
    Test the task_func function with default arguments.
    """
    df = task_func(rows=10)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, 5)
    assert set(df.columns) == set(["A", "B", "C", "D", "E"])

def test_task_func_custom_args():
    """
    Test the task_func function with custom arguments.
    """
    df = task_func(rows=5, columns=["A", "B", "C"], seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 3)
    assert set(df.columns) == set(["A", "B", "C"])
    assert (df.values == np.array([[0.37454012, 0.95071431, 0.73199394],
                                   [0.59865848, 0.15601864, 0.15599452],
                                   [0.05808361, 0.86617615, 0.60111501],
                                   [0.70807258, 0.02058449, 0.96990741],
                                   [0.83244264, 0.21233911, 0.18182497]])).all()

def test_task_func_invalid_args():
    """
    Test the task_func function with invalid arguments.
    """
    with pytest.raises(ValueError):
        task_func(rows=-1)
    with pytest.raises(TypeError):
        task_func(rows=10, columns=123)
    with pytest.raises(TypeError):
        task_func(rows=10, seed="abc")
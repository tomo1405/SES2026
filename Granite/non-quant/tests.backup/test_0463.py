import pandas as pd
import random
import pytest
from src_0463 import task_func

@pytest.mark.parametrize("num_rows", [0, 10, 100])
def test_task_func_valid_num_rows(num_rows):
    df, ax = task_func(num_rows=num_rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

@pytest.mark.parametrize("categories", [["a", "b", "c", "d", "e"], ["x", "y", "z"]])
def test_task_func_valid_categories(categories):
    df, ax = task_func(categories=categories)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_invalid_num_rows():
    with pytest.raises(ValueError):
        task_func(num_rows=-1)
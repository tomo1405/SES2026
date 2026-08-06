import matplotlib
import pandas as pd
import pytest
from src_0463 import task_func


@pytest.mark.parametrize("num_rows", [0, 1, 10, 100])
def test_task_func_valid_num_rows(num_rows):
    df, ax = task_func(num_rows=num_rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_invalid_num_rows():
    with pytest.raises(ValueError):
        task_func(num_rows=-1)

@pytest.mark.parametrize("categories", [["a", "b", "c", "d", "e"], ["x", "y", "z"]])
def test_task_func_valid_categories(categories):
    df, ax = task_func(categories=categories)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_invalid_categories():
    with pytest.raises(ValueError):
        task_func(categories=["a", "b"])

@pytest.mark.parametrize("random_seed", [42, 123, 567])
def test_task_func_valid_random_seed(random_seed):
    df1, ax1 = task_func(random_seed=random_seed)
    df2, ax2 = task_func(random_seed=random_seed)
    assert df1.equals(df2)
    assert ax1 == ax2
import matplotlib
import pandas as pd
import pytest
from src_0463 import task_func


def test_task_func_num_rows_negative():
    with pytest.raises(ValueError):
        task_func(num_rows=-1)

def test_task_func_categories_empty():
    with pytest.raises(ValueError):
        task_func(categories=[])

def test_task_func_random_seed_not_int():
    with pytest.raises(TypeError):
        task_func(random_seed="abc")

def test_task_func_return_type():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)

def test_task_func_category_counts():
    df, ax = task_func()
    assert df["Category"].value_counts().sum() == len(df)
    assert ax.get_title() == "Category Counts"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Count"
    assert ax.get_figsize() == (10, 6)
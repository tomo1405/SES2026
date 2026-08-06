import pytest
from src_0463 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_default_parameters():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 100
    assert all(col in df.columns for col in ["Category", "Value"])
    assert ax.get_title() == "Category Counts"
    plt.close(ax.figure)

def test_task_func_custom_parameters():
    num_rows = 50
    categories = ["x", "y", "z"]
    random_seed = 123
    df, ax = task_func(num_rows=num_rows, categories=categories, random_seed=random_seed)
    assert len(df) == num_rows
    assert all(category in categories for category in df["Category"].unique())
    plt.close(ax.figure)

def test_task_func_negative_num_rows():
    with pytest.raises(ValueError):
        task_func(num_rows=-10)

def test_task_func_zero_num_rows():
    with pytest.raises(ValueError):
        task_func(num_rows=0)

def test_task_func_empty_categories():
    with pytest.raises(IndexError):
        task_func(categories=[])

def test_task_func_single_category():
    df, ax = task_func(categories=["single"])
    assert all(category == "single" for category in df["Category"])
    plt.close(ax.figure)
python
import pandas as pd
import random
import pytest

from src_0463 import task_func

def test_task_func():
    # Test case 1: num_rows = 100, categories = ["a", "b", "c", "d", "e"], random_seed = 42
    df, ax = task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)
    assert df.shape == (100, 2)
    assert df["Category"].nunique() == 5
    assert df["Value"].min() >= 1
    assert df["Value"].max() <= 100
    assert ax.get_title() == "Category Counts"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Count"

    # Test case 2: num_rows = 0, categories = ["a", "b", "c", "d", "e"], random_seed = 42
    with pytest.raises(ValueError):
        task_func(num_rows=0, categories=["a", "b", "c", "d", "e"], random_seed=42)

    # Test case 3: num_rows = 100, categories = ["a", "b", "c", "d", "e"], random_seed = 0
    df, ax = task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=0)
    assert df.shape == (100, 2)
    assert df["Category"].nunique() == 5
    assert df["Value"].min() >= 1
    assert df["Value"].max() <= 100
    assert ax.get_title() == "Category Counts"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Count"

    # Test case 4: num_rows = 100, categories = ["a", "b", "c", "d", "e"], random_seed = 1
    df, ax = task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=1)
    assert df.shape == (100, 2)
    assert df["Category"].nunique() == 5
    assert df["Value"].min() >= 1
    assert df["Value"].max() <= 100
    assert ax.get_title() == "Category Counts"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Count"

    # Test case 5: num_rows = 100, categories = ["a", "b", "c", "d", "e"], random_seed = 100
    df, ax = task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=100)
    assert df.shape == (100, 2)
    assert df["Category"].nunique() == 5
    assert df["Value"].min() >= 1
    assert df["Value"].max() <= 100
    assert ax.get_title() == "Category Counts"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Count"
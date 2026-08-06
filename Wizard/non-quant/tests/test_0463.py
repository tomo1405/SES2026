python
import pandas as pd
import random
import pytest

from src_0463 import task_func

def test_task_func():
    # Test case 1: num_rows is negative
    with pytest.raises(ValueError):
        task_func(num_rows=-10)

    # Test case 2: num_rows is zero
    with pytest.raises(ValueError):
        task_func(num_rows=0)

    # Test case 3: num_rows is positive
    num_rows = 10
    categories = ["a", "b", "c", "d", "e"]
    random_seed = 42
    df, ax = task_func(num_rows=num_rows, categories=categories, random_seed=random_seed)
    assert df.shape == (num_rows, 2)
    assert ax.get_title() == "Category Counts"
    assert ax.get_xlabel() == "Category"
    assert ax.get_ylabel() == "Count"
    assert list(df["Category"]) == categories
    assert all(df["Value"] >= 1) and all(df["Value"] <= 100)
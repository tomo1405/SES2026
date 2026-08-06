python
import pandas as pd
import numpy as np
import pytest

def task_func(days, random_seed=0):
    np.random.seed(random_seed)
    date_rng = pd.date_range(start="2023-01-01", periods=days, freq="D")
    df = pd.DataFrame(date_rng, columns=["date"])
    df.set_index("date", inplace=True)
    categories = ["Groceries", "Entertainment", "Rent", "Utilities", "Miscellaneous"]
    for category in categories:
        df[category] = np.random.randint(0, 100, size=(days))

    return df

def test_task_func():
    # Test case 1: days=10, random_seed=0
    df = task_func(10, 0)
    assert df.shape == (10, 6)
    assert df.index.name == "date"
    assert df.columns.tolist() == ["date", "Groceries", "Entertainment", "Rent", "Utilities", "Miscellaneous"]
    assert df.loc[df.index[0], "Groceries"] == 21
    assert df.loc[df.index[0], "Entertainment"] == 11
    assert df.loc[df.index[0], "Rent"] == 35
    assert df.loc[df.index[0], "Utilities"] == 78
    assert df.loc[df.index[0], "Miscellaneous"] == 85

    # Test case 2: days=5, random_seed=1
    df = task_func(5, 1)
    assert df.shape == (5, 6)
    assert df.index.name == "date"
    assert df.columns.tolist() == ["date", "Groceries", "Entertainment", "Rent", "Utilities", "Miscellaneous"]
    assert df.loc[df.index[0], "Groceries"] == 6
    assert df.loc[df.index[0], "Entertainment"] == 19
    assert df.loc[df.index[0], "Rent"] == 8
    assert df.loc[df.index[0], "Utilities"] == 31
    assert df.loc[df.index[0], "Miscellaneous"] == 66
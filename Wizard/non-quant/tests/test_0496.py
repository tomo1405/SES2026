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
    # Test with default random seed
    df = task_func(10)
    assert df.shape == (10, 5)
    assert df.index.name == "date"
    assert df.columns.tolist() == ["date", "Groceries", "Entertainment", "Rent", "Utilities"]
    assert df.iloc[0]["Groceries"] == 21
    assert df.iloc[0]["Entertainment"] == 71
    assert df.iloc[0]["Rent"] == 79
    assert df.iloc[0]["Utilities"] == 15

    # Test with custom random seed
    df = task_func(10, random_seed=42)
    assert df.shape == (10, 5)
    assert df.index.name == "date"
    assert df.columns.tolist() == ["date", "Groceries", "Entertainment", "Rent", "Utilities"]
    assert df.iloc[0]["Groceries"] == 21
    assert df.iloc[0]["Entertainment"] == 71
    assert df.iloc[0]["Rent"] == 79
    assert df.iloc[0]["Utilities"] == 15
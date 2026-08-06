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
    assert df.index[0] == pd.Timestamp("2023-01-01")
    assert df.index[-1] == pd.Timestamp("2023-01-10")
    assert df["Groceries"].sum() == 455
    assert df["Entertainment"].sum() == 211
    assert df["Rent"].sum() == 61
    assert df["Utilities"].sum() == 76
    assert df["Miscellaneous"].sum() == 89

    # Test with custom random seed
    df = task_func(10, random_seed=42)
    assert df.shape == (10, 5)
    assert df.index[0] == pd.Timestamp("2023-01-01")
    assert df.index[-1] == pd.Timestamp("2023-01-10")
    assert df["Groceries"].sum() == 455
    assert df["Entertainment"].sum() == 211
    assert df["Rent"].sum() == 61
    assert df["Utilities"].sum() == 76
    assert df["Miscellaneous"].sum() == 89

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func(-1)
import pandas as pd
from src_0496 import task_func


def test_task_func_output_shape():
    days = 10
    df = task_func(days)
    assert df.shape == (days, 5), f"Expected shape {(days, 5)}, but got {df.shape}"

def test_task_func_date_range():
    days = 5
    df = task_func(days)
    expected_dates = pd.date_range(start="2023-01-01", periods=days, freq="D")
    assert all(df.index == expected_dates), "Date range does not match expected dates"

def test_task_func_categories():
    days = 1
    df = task_func(days)
    expected_categories = ["Groceries", "Entertainment", "Rent", "Utilities", "Miscellaneous"]
    assert list(df.columns) == expected_categories, "Categories do not match expected categories"

def test_task_func_random_values():
    days = 1
    df = task_func(days)
    for category in df.columns:
        assert df[category].values[0] >= 0 and df[category].values[0] < 100, "Random values are out of expected range"

def test_task_func_default_random_seed():
    days = 1
    df1 = task_func(days)
    df2 = task_func(days)
    assert df1.equals(df2), "Dataframes with default random seed should be identical"

def test_task_func_custom_random_seed():
    days = 1
    df1 = task_func(days, random_seed=1)
    df2 = task_func(days, random_seed=2)
    assert not df1.equals(df2), "Dataframes with different random seeds should not be identical"
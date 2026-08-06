import pytest
from src_0493 import task_func
import pandas as pd
from datetime import datetime

def test_task_func_valid_input():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000)
    df = task_func(epoch_milliseconds)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[1] == 3
    assert all(df.columns == ["Product", "Date", "Sales"])
    assert len(df["Product"].unique()) == 5
    assert all(df["Date"] >= datetime.fromtimestamp(epoch_milliseconds / 1000.0))
    assert all(df["Date"] <= datetime.now())
    assert all(df["Sales"].between(10, 50))

def test_task_func_invalid_products_length():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000)
    with pytest.raises(ValueError, match="Products must contain 5 unique items"):
        task_func(epoch_milliseconds, products=["Product1", "Product2"])

def test_task_func_start_time_after_end_time():
    epoch_milliseconds = int((datetime.now() + pd.Timedelta(days=1)).timestamp() * 1000)
    with pytest.raises(ValueError, match="Start time must be before current system time"):
        task_func(epoch_milliseconds)

def test_task_func_random_seed_consistency():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000)
    random_seed = 42
    df1 = task_func(epoch_milliseconds, random_seed=random_seed)
    df2 = task_func(epoch_milliseconds, random_seed=random_seed)
    assert df1.equals(df2)

def test_task_func_with_custom_products():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000)
    custom_products = ["ProductA", "ProductB", "ProductC", "ProductD", "ProductE"]
    df = task_func(epoch_milliseconds, products=custom_products)
    assert all(df["Product"].isin(custom_products))
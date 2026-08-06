import pandas as pd
from datetime import datetime
import random
import pytest

from src_0493 import task_func

def test_task_func():
    epoch_milliseconds = 1640995200000
    random_seed = 0
    products = ["Product1", "Product2", "Product3", "Product4", "Product5"]
    df = task_func(epoch_milliseconds, random_seed, products)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (180, 3)
    assert df.columns.tolist() == ["Product", "Date", "Sales"]
    assert df["Product"].nunique() == 5
    assert df["Date"].min() == datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    assert df["Date"].max() == datetime.now()
    assert df["Sales"].min() >= 10
    assert df["Sales"].max() <= 50

def test_task_func_invalid_products():
    with pytest.raises(ValueError, match="Products must contain 5 unique items"):
        epoch_milliseconds = 1640995200000
        random_seed = 0
        products = ["Product1", "Product2", "Product3", "Product4"]
        task_func(epoch_milliseconds, random_seed, products)

def test_task_func_invalid_start_time():
    with pytest.raises(ValueError, match="Start time must be before current system time"):
        epoch_milliseconds = 1640995200000
        random_seed = 0
        products = ["Product1", "Product2", "Product3", "Product4", "Product5"]
        task_func(epoch_milliseconds + 1000, random_seed, products)
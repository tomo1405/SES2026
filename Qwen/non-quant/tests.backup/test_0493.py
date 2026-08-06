import pytest
from src_0493 import task_func
import pandas as pd
from datetime import datetime, timedelta

def test_task_func_with_valid_input():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # One day ago
    df = task_func(epoch_milliseconds)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[1] == 3
    assert df.columns.tolist() == ["Product", "Date", "Sales"]
    assert len(df) == 5 * (datetime.now().date() - datetime.fromtimestamp(epoch_milliseconds / 1000).date()).days + 1
    assert all(df['Product'].isin(["Product1", "Product2", "Product3", "Product4", "Product5"]))
    assert all(df['Sales'].between(10, 50))

def test_task_func_with_invalid_products_length():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # One day ago
    with pytest.raises(ValueError, match="Products must contain 5 unique items"):
        task_func(epoch_milliseconds, products=["Product1", "Product2"])

def test_task_func_with_start_time_after_end_time():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) + 86400000  # One day from now
    with pytest.raises(ValueError, match="Start time must be before current system time"):
        task_func(epoch_milliseconds)

def test_task_func_with_random_seed():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # One day ago
    df1 = task_func(epoch_milliseconds, random_seed=42)
    df2 = task_func(epoch_milliseconds, random_seed=42)
    assert df1.equals(df2)

def test_task_func_with_unique_products():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # One day ago
    df = task_func(epoch_milliseconds, products=["ProductA", "ProductB", "ProductC", "ProductD", "ProductE"])
    assert len(df) == 5 * (datetime.now().date() - datetime.fromtimestamp(epoch_milliseconds / 1000).date()).days + 1
    assert all(df['Product'].isin(["ProductA", "ProductB", "ProductC", "ProductD", "ProductE"]))

def test_task_func_with_no_products():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # One day ago
    with pytest.raises(ValueError, match="Products must contain 5 unique items"):
        task_func(epoch_milliseconds, products=[])

def test_task_func_with_duplicate_products():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # One day ago
    with pytest.raises(ValueError, match="Products must contain 5 unique items"):
        task_func(epoch_milliseconds, products=["Product1", "Product1", "Product2", "Product3", "Product4"])
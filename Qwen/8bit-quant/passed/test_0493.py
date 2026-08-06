import pytest
from src_0493 import task_func
import pandas as pd
from datetime import datetime, timedelta

def test_task_func_with_valid_input():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # 1 day ago
    df = task_func(epoch_milliseconds)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5 * (datetime.now().date() - datetime.fromtimestamp(epoch_milliseconds / 1000).date()).days + 5
    assert all(df['Product'].isin(["Product1", "Product2", "Product3", "Product4", "Product5"]))
    assert all(df['Sales'] >= 10) and all(df['Sales'] <= 50)
    assert all(df['Date'] >= datetime.fromtimestamp(epoch_milliseconds / 1000)) and all(df['Date'] <= datetime.now())

def test_task_func_with_invalid_products_length():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # 1 day ago
    with pytest.raises(ValueError, match="Products must contain 5 unique items"):
        task_func(epoch_milliseconds, products=["Product1", "Product2"])

def test_task_func_with_start_date_after_end_date():
    epoch_milliseconds = int((datetime.now() + timedelta(days=1)).timestamp() * 1000)  # 1 day from now
    with pytest.raises(ValueError, match="Start time must be before current system time"):
        task_func(epoch_milliseconds)

def test_task_func_with_random_seed():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # 1 day ago
    df1 = task_func(epoch_milliseconds, random_seed=42)
    df2 = task_func(epoch_milliseconds, random_seed=42)
    assert df1.equals(df2)

def test_task_func_with_unique_products():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 86400000  # 1 day ago
    df = task_func(epoch_milliseconds, products=["ProductA", "ProductB", "ProductC", "ProductD", "ProductE"])
    assert len(df) == 5 * (datetime.now().date() - datetime.fromtimestamp(epoch_milliseconds / 1000).date()).days + 5
    assert all(df['Product'].isin(["ProductA", "ProductB", "ProductC", "ProductD", "ProductE"]))
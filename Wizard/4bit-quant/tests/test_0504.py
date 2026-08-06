python
import numpy as np
import pandas as pd
from datetime import datetime
import pytest

def task_func(
    days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=0
):
    np.random.seed(random_seed)

    if not isinstance(days_in_past, int) or days_in_past <= 0:
        raise ValueError("days_in_past must be a positive integer.")
    if not stock_names or not all(isinstance(name, str) for name in stock_names):
        raise ValueError("stock_names must be a list of strings and cannot be empty.")

    dates = pd.date_range(end=datetime.now().date(), periods=days_in_past)
    prices = np.random.rand(days_in_past, len(stock_names)) * 100
    df = pd.DataFrame(prices, columns=stock_names, index=dates)

    return df

def test_task_func():
    # Test with default arguments
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7, 5)
    assert df.columns.tolist() == ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
    assert df.index.tolist() == [
        datetime.now().date() - timedelta(days=i) for i in range(6, -1, -1)
    ]

    # Test with custom arguments
    df = task_func(days_in_past=30, stock_names=["TSLA", "AAPL", "GOOGL"], random_seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (30, 3)
    assert df.columns.tolist() == ["TSLA", "AAPL", "GOOGL"]
    assert df.index.tolist() == [
        datetime.now().date() - timedelta(days=i) for i in range(29, -1, -1)
    ]

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(days_in_past=-1)
    with pytest.raises(ValueError):
        task_func(days_in_past="7")
    with pytest.raises(ValueError):
        task_func(stock_names=[])
    with pytest.raises(ValueError):
        task_func(stock_names=["AAPL", 123])
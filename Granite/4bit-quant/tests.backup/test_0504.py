import pytest
import numpy as np
import pandas as pd
from datetime import datetime

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
    # Test case 1: days_in_past is not an integer
    with pytest.raises(ValueError) as exc_info:
        task_func(days_in_past='7', stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"])
    assert "days_in_past must be a positive integer." in str(exc_info.value)

    # Test case 2: days_in_past is not positive
    with pytest.raises(ValueError) as exc_info:
        task_func(days_in_past=0, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"])
    assert "days_in_past must be a positive integer." in str(exc_info.value)

    # Test case 3: stock_names is not a list of strings
    with pytest.raises(ValueError) as exc_info:
        task_func(days_in_past=7, stock_names="AAPL")
    assert "stock_names must be a list of strings and cannot be empty." in str(exc_info.value)

    # Test case 4: stock_names is an empty list
    with pytest.raises(ValueError) as exc_info:
        task_func(days_in_past=7, stock_names=[])
    assert "stock_names must be a list of strings and cannot be empty." in str(exc_info.value)

    # Test case 5: stock_names contains non-string elements
    with pytest.raises(ValueError) as exc_info:
        task_func(days_in_past=7, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", 123])
    assert "stock_names must be a list of strings and cannot be empty." in str(exc_info.value)

    # Test case 6: Default arguments
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7, 5)
    assert list(df.columns) == ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
    assert df.index[0] == datetime.now().date()

    # Test case 7: Custom arguments
    df = task_func(days_in_past=10, stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB"], random_seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, 5)
    assert list(df.columns) == ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
    assert df.index[0] == datetime.now().date()
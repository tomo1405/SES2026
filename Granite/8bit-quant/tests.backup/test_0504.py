import pytest
import numpy as np
import pandas as pd
from datetime import datetime
from src_0504 import task_func

def test_task_func_valid_input():
    """
    Test valid input for task_func.
    """
    days_in_past = 7
    stock_names = ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]
    random_seed = 0
    df = task_func(days_in_past, stock_names, random_seed)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (days_in_past, len(stock_names))

def test_task_func_invalid_days_in_past():
    """
    Test invalid input for days_in_past for task_func.
    """
    with pytest.raises(ValueError) as exc_info:
        task_func(0, ["AAPL"], 0)
    assert "days_in_past must be a positive integer." in str(exc_info.value)

def test_task_func_invalid_stock_names():
    """
    Test invalid input for stock_names for task_func.
    """
    with pytest.raises(ValueError) as exc_info:
        task_func(7, [1, 2, 3], 0)
    assert "stock_names must be a list of strings and cannot be empty." in str(exc_info.value)
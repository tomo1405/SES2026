import pandas as pd
from datetime import datetime
import random
import pytest
from src_0493 import task_func

def test_task_func_valid_input():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000)
    random_seed = 0
    products = ["Product1", "Product2", "Product3", "Product4", "Product5"]
    df = task_func(epoch_milliseconds, random_seed, products)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (365 * 5, 3)
    assert df.columns.tolist() == ["Product", "Date", "Sales"]

def test_task_func_invalid_products():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000)
    random_seed = 0
    products = ["Product1", "Product2", "Product3", "Product4", "Product5", "Product6"]
    with pytest.raises(ValueError) as exc_info:
        task_func(epoch_milliseconds, random_seed, products)
    assert str(exc_info.value) == "Products must contain 5 unique items"

def test_task_func_invalid_start_time():
    epoch_milliseconds = int(datetime.now().timestamp() * 1000) - 1000
    random_seed = 0
    products = ["Product1", "Product2", "Product3", "Product4", "Product5"]
    with pytest.raises(ValueError) as exc_info:
        task_func(epoch_milliseconds, random_seed, products)
    assert str(exc_info.value) == "Start time must be before current system time"
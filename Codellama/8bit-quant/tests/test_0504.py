from datetime import datetime

import numpy as np
import pandas as pd
import pytest
from src_0504 import task_func


def test_task_func_days_in_past_type():
    with pytest.raises(ValueError):
        task_func(days_in_past="7")

def test_task_func_days_in_past_value():
    with pytest.raises(ValueError):
        task_func(days_in_past=0)

def test_task_func_stock_names_type():
    with pytest.raises(ValueError):
        task_func(stock_names=["AAPL", "GOOGL", "MSFT", "AMZN", "FB", 0])

def test_task_func_stock_names_value():
    with pytest.raises(ValueError):
        task_func(stock_names=[])

def test_task_func_random_seed_type():
    with pytest.raises(ValueError):
        task_func(random_seed="0")

def test_task_func_random_seed_value():
    with pytest.raises(ValueError):
        task_func(random_seed=-1)

def test_task_func_output_type():
    assert isinstance(task_func(), pd.DataFrame)

def test_task_func_output_shape():
    assert task_func().shape == (7, 5)

def test_task_func_output_columns():
    assert task_func().columns.tolist() == ["AAPL", "GOOGL", "MSFT", "AMZN", "FB"]

def test_task_func_output_index():
    assert task_func().index.tolist() == pd.date_range(end=datetime.now().date(), periods=7).tolist()

def test_task_func_output_values():
    assert np.all(task_func().values >= 0)
    assert np.all(task_func().values <= 100)
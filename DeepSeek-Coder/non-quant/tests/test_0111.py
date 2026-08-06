import pytest
from src_0111 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    data = {
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Sales': [10, 20, 30]
    }
    df = pd.DataFrame(data)
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result is not None

def test_task_func_invalid_input():
    df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-02'], 'Sales': [10, 20]})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_empty_data():
    df = pd.DataFrame({'Date': [], 'Sales': []})
    with pytest.raises(ValueError):
        task_func(df)
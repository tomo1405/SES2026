python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0743 import task_func

def test_task_func_empty_input():
    with pytest.raises(Exception):
        task_func([])

def test_task_func_non_numeric_values():
    with pytest.raises(ValueError):
        task_func([('A', 'B'), ('C', 'D')])

def test_task_func_valid_input():
    df = task_func([('A', 1), ('B', 2), ('C', 3)])
    assert df.shape == (3, 2)
    assert df.Category.tolist() == ['A', 'B', 'C']
    assert df.Value.tolist() == [0.0, 0.5, 1.0]
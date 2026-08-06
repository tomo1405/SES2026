import pytest
from src_0317 import task_func
import pandas as pd

def test_task_func_return_type():
    result = task_func()
    assert isinstance(result, pd.DataFrame), "The function should return a pandas DataFrame."

def test_task_func_columns():
    result = task_func()
    expected_columns = ['Category', 'Count']
    assert list(result.columns) == expected_columns, "The DataFrame should have the correct columns."

def test_task_func_categories():
    result = task_func()
    expected_categories = set(['A', 'B', 'C', 'D', 'E'])
    assert set(result['Category']) == expected_categories, "The DataFrame should contain the correct categories."

def test_task_func_count_values():
    result = task_func((0, 100))
    counts = result['Count'].values
    assert all(0 <= count <= 100 for count in counts), "Count values should be within the specified range."

def test_task_func_randomness():
    result1 = task_func()
    result2 = task_func()
    assert not result1.equals(result2), "Function should produce different results on each call due to randomness."
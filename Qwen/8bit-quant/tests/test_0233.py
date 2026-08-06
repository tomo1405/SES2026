import pytest
from src_0233 import task_func
import pandas as pd

def test_task_func_with_valid_data():
    data = {
        'Customer': ['A', 'B', 'A', 'C'],
        'Sales': [100, 200, 150, 300],
        'Category': ['X', 'Y', 'X', 'Z']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result == {'Total Sales': 750, 'Most Popular Category': 'X'}

def test_task_func_with_no_data():
    df = pd.DataFrame(columns=['Customer', 'Sales', 'Category'])
    result = task_func(df)
    assert result == {'Total Sales': 0, 'Most Popular Category': None}

def test_task_func_with_one_unique_customer():
    data = {
        'Customer': ['A', 'A', 'A'],
        'Sales': [100, 150, 200],
        'Category': ['X', 'Y', 'X']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result == {'Total Sales': 450, 'Most Popular Category': 'X'}

def test_task_func_with_all_categories_same():
    data = {
        'Customer': ['A', 'B', 'C', 'D'],
        'Sales': [100, 200, 300, 400],
        'Category': ['X', 'X', 'X', 'X']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result == {'Total Sales': 1000, 'Most Popular Category': 'X'}

def test_task_func_with_non_dataframe_input():
    with pytest.raises(ValueError) as excinfo:
        task_func([1, 2, 3])
    assert str(excinfo.value) == "The input df is not a DataFrame"
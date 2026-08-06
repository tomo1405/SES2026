import pytest
from src_0233 import task_func
import pandas as pd

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['Customer', 'Sales', 'Category'])
    result = task_func(df)
    assert result == {'Total Sales': 0, 'Most Popular Category': None}

def test_task_func_single_row():
    data = {
        'Customer': ['A'],
        'Sales': [100],
        'Category': ['Electronics']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result == {'Total Sales': 100, 'Most Popular Category': 'Electronics'}

def test_task_func_multiple_rows_same_customer():
    data = {
        'Customer': ['A', 'A', 'B'],
        'Sales': [100, 50, 200],
        'Category': ['Electronics', 'Electronics', 'Clothing']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result == {'Total Sales': 350, 'Most Popular Category': 'Electronics'}

def test_task_func_multiple_rows_different_customers():
    data = {
        'Customer': ['A', 'B', 'C'],
        'Sales': [100, 200, 300],
        'Category': ['Electronics', 'Clothing', 'Books']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result == {'Total Sales': 600, 'Most Popular Category': 'Electronics'}

def test_task_func_no_sales():
    data = {
        'Customer': ['A', 'B'],
        'Sales': [0, 0],
        'Category': ['Electronics', 'Clothing']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result == {'Total Sales': 0, 'Most Popular Category': 'Electronics'}

def test_task_func_most_popular_category_tie():
    data = {
        'Customer': ['A', 'B', 'C'],
        'Sales': [100, 200, 300],
        'Category': ['Electronics', 'Clothing', 'Electronics']
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert result == {'Total Sales': 600, 'Most Popular Category': 'Electronics'}
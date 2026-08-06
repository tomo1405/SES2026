import pandas as pd
import pytest
from src_0233 import task_func

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Customer': ['A', 'B', 'C', 'D', 'E'],
        'Sales': [100, 200, 150, 300, 250],
        'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics']
    })

def test_task_func_valid_input(sample_df):
    assert task_func(sample_df) == {'Total Sales': 900, 'Most Popular Category': 'Electronics'}

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func('invalid input')

def test_task_func_no_duplicates(sample_df):
    sample_df = sample_df.drop_duplicates(subset='Customer')
    assert task_func(sample_df) == {'Total Sales': 900, 'Most Popular Category': 'Electronics'}

def test_task_func_no_sales(sample_df):
    sample_df = sample_df.drop('Sales', axis=1)
    with pytest.raises(KeyError):
        task_func(sample_df)

def test_task_func_no_category(sample_df):
    sample_df = sample_df.drop('Category', axis=1)
    with pytest.raises(KeyError):
        task_func(sample_df)
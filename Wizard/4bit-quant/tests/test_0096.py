python
import pandas as pd
import random
import pytest

from src_0096 import task_func

def test_task_func():
    # Test case 1: Test with default values
    sales_df = task_func()
    assert isinstance(sales_df, pd.DataFrame)
    assert len(sales_df) == 12 * 5
    assert set(sales_df['Category'].unique()) == set(['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty & Personal Care'])
    assert set(sales_df['Month'].unique()) == set(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    assert sales_df['Sales'].min() >= 100
    assert sales_df['Sales'].max() <= 500

    # Test case 2: Test with custom values
    categories = ['Electronics', 'Clothing']
    months = ['January', 'February', 'March']
    random_seed = 123
    sales_df = task_func(categories=categories, months=months, random_seed=random_seed)
    assert isinstance(sales_df, pd.DataFrame)
    assert len(sales_df) == 3 * 2
    assert set(sales_df['Category'].unique()) == set(['Electronics', 'Clothing'])
    assert set(sales_df['Month'].unique()) == set(['January', 'February', 'March'])
    assert sales_df['Sales'].min() >= 100
    assert sales_df['Sales'].max() <= 500

    # Test case 3: Test with invalid values
    with pytest.raises(ValueError):
        task_func(categories=123, months=None, random_seed=42)
    with pytest.raises(ValueError):
        task_func(categories=[], months=None, random_seed=42)
    with pytest.raises(ValueError):
        task_func(categories=None, months=123, random_seed=42)
    with pytest.raises(ValueError):
        task_func(categories=None, months=[], random_seed=42)
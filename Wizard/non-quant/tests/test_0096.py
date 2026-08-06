python
import pandas as pd
import random
import pytest

from src_0096 import task_func

def test_task_func():
    # Test with default arguments
    sales_df = task_func()
    assert isinstance(sales_df, pd.DataFrame)
    assert len(sales_df) == 12 * 5
    assert set(sales_df['Category'].unique()) == set(['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty & Personal Care'])
    assert set(sales_df['Month'].unique()) == set(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    assert sales_df['Sales'].min() >= 100
    assert sales_df['Sales'].max() <= 500

    # Test with custom arguments
    categories = ['A', 'B', 'C']
    months = ['X', 'Y', 'Z']
    random_seed = 123
    sales_df = task_func(categories=categories, months=months, random_seed=random_seed)
    assert isinstance(sales_df, pd.DataFrame)
    assert len(sales_df) == 3 * 3
    assert set(sales_df['Category'].unique()) == set(categories)
    assert set(sales_df['Month'].unique()) == set(months)
    assert sales_df['Sales'].min() >= 100
    assert sales_df['Sales'].max() <= 500

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(categories=123)
    with pytest.raises(ValueError):
        task_func(categories=[])
    with pytest.raises(ValueError):
        task_func(months=123)
    with pytest.raises(ValueError):
        task_func(months=[])
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
    assert set(sales_df['Month']) == set(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    assert set(sales_df['Category']) == set(['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty & Personal Care'])
    assert all(sales_df['Sales'] >= 100) and all(sales_df['Sales'] <= 500)

    # Test with custom arguments
    categories = ['Electronics', 'Clothing']
    months = ['January', 'February', 'March']
    sales_df = task_func(categories=categories, months=months)
    assert isinstance(sales_df, pd.DataFrame)
    assert len(sales_df) == 3 * 2
    assert set(sales_df['Month']) == set(['January', 'February', 'March'])
    assert set(sales_df['Category']) == set(['Electronics', 'Clothing'])
    assert all(sales_df['Sales'] >= 100) and all(sales_df['Sales'] <= 500)

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(categories='Electronics', months=['January', 'February', 'March'])
    with pytest.raises(ValueError):
        task_func(categories=['Electronics', 'Clothing'], months='January')
    with pytest.raises(ValueError):
        task_func(categories=[], months=['January', 'February', 'March'])
    with pytest.raises(ValueError):
        task_func(categories=['Electronics', 'Clothing'], months=[])
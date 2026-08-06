import pytest
from src_0096 import task_func
import pandas as pd

def test_task_func_default_values():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 60  # 12 months * 5 categories
    assert all(df.columns == ['Month', 'Category', 'Sales'])

def test_task_func_custom_categories():
    custom_categories = ['Toys', 'Sports']
    df = task_func(categories=custom_categories)
    assert len(df) == 24  # 12 months * 2 custom categories
    assert all(df['Category'].isin(custom_categories))

def test_task_func_custom_months():
    custom_months = ['January', 'February']
    df = task_func(months=custom_months)
    assert len(df) == 10  # 2 custom months * 5 categories
    assert all(df['Month'].isin(custom_months))

def test_task_func_custom_categories_and_months():
    custom_categories = ['Toys', 'Sports']
    custom_months = ['January', 'February']
    df = task_func(categories=custom_categories, months=custom_months)
    assert len(df) == 4  # 2 custom months * 2 custom categories
    assert all(df['Category'].isin(custom_categories))
    assert all(df['Month'].isin(custom_months))

def test_task_func_invalid_categories():
    with pytest.raises(ValueError):
        task_func(categories=[])

def test_task_func_invalid_months():
    with pytest.raises(ValueError):
        task_func(months=[])

def test_task_func_non_list_categories():
    with pytest.raises(ValueError):
        task_func(categories='Not a list')

def test_task_func_non_list_months():
    with pytest.raises(ValueError):
        task_func(months='Not a list')

def test_task_func_random_seed_reproducibility():
    df1 = task_func(random_seed=42)
    df2 = task_func(random_seed=42)
    assert df1.equals(df2)
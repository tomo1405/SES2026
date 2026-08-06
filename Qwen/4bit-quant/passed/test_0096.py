import pytest
from src_0096 import task_func
import pandas as pd

def test_task_func_default_parameters():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 12 * 5  # 12 months * 5 categories
    assert all(col in df.columns for col in ['Month', 'Category', 'Sales'])

def test_task_func_custom_categories_and_months():
    categories = ['Toys', 'Games']
    months = ['January', 'February']
    df = task_func(categories=categories, months=months)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2 * 2  # 2 months * 2 categories
    assert all(col in df.columns for col in ['Month', 'Category', 'Sales'])

def test_task_func_invalid_categories():
    with pytest.raises(ValueError):
        task_func(categories=[])

def test_task_func_invalid_months():
    with pytest.raises(ValueError):
        task_func(months=[])

def test_task_func_sales_values():
    df = task_func()
    assert df['Sales'].between(100, 500).all()

def test_task_func_reproducibility():
    df1 = task_func(random_seed=42)
    df2 = task_func(random_seed=42)
    assert df1.equals(df2)
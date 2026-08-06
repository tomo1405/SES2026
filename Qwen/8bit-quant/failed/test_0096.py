import pytest
from src_0096 import task_func

def test_task_func_default_parameters():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 60  # 12 months * 5 categories
    assert all(column in df.columns for column in ['Month', 'Category', 'Sales'])

def test_task_func_custom_categories_and_months():
    custom_categories = ['Toys', 'Sports']
    custom_months = ['January', 'February']
    df = task_func(categories=custom_categories, months=custom_months)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 4  # 2 months * 2 categories
    assert all(column in df.columns for column in ['Month', 'Category', 'Sales'])

def test_task_func_invalid_categories():
    with pytest.raises(ValueError):
        task_func(categories=[])

def test_task_func_invalid_months():
    with pytest.raises(ValueError):
        task_func(months=[])

def test_task_func_non_list_categories():
    with pytest.raises(ValueError):
        task_func(categories="Not a list")

def test_task_func_non_list_months():
    with pytest.raises(ValueError):
        task_func(months="Not a list")

def test_task_func_reproducibility():
    df1 = task_func(random_seed=42)
    df2 = task_func(random_seed=42)
    assert df1.equals(df2)

def test_task_func_random_sales_values():
    df = task_func()
    sales_values = df['Sales'].tolist()
    assert all(100 <= sale < 501 for sale in sales_values)
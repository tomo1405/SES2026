import pytest
from src_0787 import task_func
import pandas as pd
import os

def test_task_func_no_output_path():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert {'Country', 'Product', 'Sales'}.issubset(df.columns)

def test_task_func_with_output_path(tmpdir):
    output_path = str(tmpdir.join('sales_data.csv'))
    df = task_func(5, output_path=output_path)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert {'Country', 'Product', 'Sales'}.issubset(df.columns)
    assert os.path.exists(output_path)

def test_task_func_random_seed():
    df1 = task_func(5, random_seed=42)
    df2 = task_func(5, random_seed=42)
    pd.testing.assert_frame_equal(df1, df2)

def test_task_func_custom_countries_products():
    countries = ['France', 'Japan']
    products = ['Product X', 'Product Y']
    df = task_func(5, countries=countries, products=products)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert {'Country', 'Product', 'Sales'}.issubset(df.columns)
    assert all(country in countries for country in df['Country'])
    assert all(product in products for product in df['Product'])

def test_task_func_sales_range():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(1 <= sales <= 100 for sales in df['Sales'])
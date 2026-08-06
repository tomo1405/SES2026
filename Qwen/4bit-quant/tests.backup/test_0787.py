import pytest
from src_0787 import task_func
import pandas as pd
import os

def test_task_func_default_output():
    result_df = task_func(5)
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == 5
    assert all(col in result_df.columns for col in ['Country', 'Product', 'Sales'])

def test_task_func_with_random_seed():
    df1 = task_func(5, random_seed=42)
    df2 = task_func(5, random_seed=42)
    assert df1.equals(df2)

def test_task_func_with_custom_countries_and_products():
    countries = ['France', 'Italy']
    products = ['Product X', 'Product Y']
    result_df = task_func(3, countries=countries, products=products)
    assert all(country in countries for country in result_df['Country'])
    assert all(product in products for product in result_df['Product'])

def test_task_func_with_output_path(tmpdir):
    output_path = str(tmpdir / 'sales_data.csv')
    task_func(3, output_path=output_path)
    assert os.path.exists(output_path)
    with open(output_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        assert rows[0] == ['Country', 'Product', 'Sales']
        assert len(rows) == 4  # Header + 3 rows of data

def test_task_func_no_output_path():
    result_df = task_func(3, output_path=None)
    assert isinstance(result_df, pd.DataFrame)
    assert len(result_df) == 3

def test_task_func_empty_countries_list():
    with pytest.raises(ValueError):
        task_func(1, countries=[])

def test_task_func_empty_products_list():
    with pytest.raises(ValueError):
        task_func(1, products=[])
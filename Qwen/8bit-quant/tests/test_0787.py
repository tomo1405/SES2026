import pytest
from src_0787 import task_func
import pandas as pd

def test_task_func_no_output():
    df = task_func(5)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert {'Country', 'Product', 'Sales'}.issubset(df.columns)

def test_task_func_with_output(tmpdir):
    output_path = tmpdir.join('sales_data.csv')
    df = task_func(5, output_path=str(output_path))
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert {'Country', 'Product', 'Sales'}.issubset(df.columns)
    assert output_path.exists()

def test_task_func_random_seed():
    df1 = task_func(5, random_seed=42)
    df2 = task_func(5, random_seed=42)
    assert df1.equals(df2)

def test_task_func_custom_countries_products():
    df = task_func(3, countries=['France', 'Italy'], products=['Product X', 'Product Y'])
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert {'Country', 'Product', 'Sales'}.issubset(df.columns)
    assert all(df['Country'].isin(['France', 'Italy']))
    assert all(df['Product'].isin(['Product X', 'Product Y']))

def test_task_func_zero_records():
    df = task_func(0)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0
    assert {'Country', 'Product', 'Sales'}.issubset(df.columns)
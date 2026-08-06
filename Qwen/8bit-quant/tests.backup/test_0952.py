import pytest
from src_0952 import task_func

def test_task_func_output_type():
    mystrings = ["Product A", "Product B"]
    n_products = 5
    result = task_func(mystrings, n_products)
    assert isinstance(result, pd.DataFrame)

def test_task_func_columns():
    mystrings = ["Product A", "Product B"]
    n_products = 5
    result = task_func(mystrings, n_products)
    expected_columns = ['Product Name', 'Category', 'Price']
    assert list(result.columns) == expected_columns

def test_task_func_number_of_rows():
    mystrings = ["Product A", "Product B"]
    n_products = 5
    result = task_func(mystrings, n_products)
    assert len(result) == n_products

def test_task_func_product_names():
    mystrings = ["Product A", "Product B"]
    n_products = 5
    result = task_func(mystrings, n_products)
    product_names = result['Product Name'].tolist()
    for name in product_names:
        assert name in [s.replace(' ', '_') for s in mystrings]

def test_task_func_categories():
    mystrings = ["Product A", "Product B"]
    n_products = 5
    result = task_func(mystrings, n_products)
    categories = result['Category'].tolist()
    for category in categories:
        assert category in ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def test_task_func_price_range():
    mystrings = ["Product A", "Product B"]
    n_products = 5
    result = task_func(mystrings, n_products)
    prices = result['Price'].tolist()
    for price in prices:
        assert 40 <= price <= 60

def test_task_func_seed_consistency():
    mystrings = ["Product A", "Product B"]
    n_products = 5
    seed_value = 0
    result1 = task_func(mystrings, n_products, seed=seed_value)
    result2 = task_func(mystrings, n_products, seed=seed_value)
    assert result1.equals(result2)
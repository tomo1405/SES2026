import pytest
from src_0952 import task_func

def test_task_func():
    # Test with default seed
    mystrings = ['Product 1', 'Product 2', 'Product 3']
    n_products = 3
    expected_data = [
        ['Product_1', 'Electronics', 50.0],
        ['Product_2', 'Clothing', 50.0],
        ['Product_3', 'Home & Kitchen', 50.0]
    ]
    result = task_func(mystrings, n_products)
    assert result.equals(expected_data)

    # Test with custom seed
    mystrings = ['Product 1', 'Product 2', 'Product 3']
    n_products = 3
    expected_data = [
        ['Product_1', 'Electronics', 50.0],
        ['Product_2', 'Clothing', 50.0],
        ['Product_3', 'Home & Kitchen', 50.0]
    ]
    result = task_func(mystrings, n_products, seed=1234)
    assert result.equals(expected_data)

    # Test with different number of products
    mystrings = ['Product 1', 'Product 2', 'Product 3']
    n_products = 5
    expected_data = [
        ['Product_1', 'Electronics', 50.0],
        ['Product_2', 'Clothing', 50.0],
        ['Product_3', 'Home & Kitchen', 50.0],
        ['Product_1', 'Electronics', 50.0],
        ['Product_2', 'Clothing', 50.0]
    ]
    result = task_func(mystrings, n_products)
    assert result.equals(expected_data)

    # Test with different number of strings
    mystrings = ['Product 1', 'Product 2', 'Product 3', 'Product 4']
    n_products = 3
    expected_data = [
        ['Product_1', 'Electronics', 50.0],
        ['Product_2', 'Clothing', 50.0],
        ['Product_3', 'Home & Kitchen', 50.0]
    ]
    result = task_func(mystrings, n_products)
    assert result.equals(expected_data)
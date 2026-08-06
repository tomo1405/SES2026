import pytest
from src_0787 import task_func

def test_task_func():
    # Test case 1: Test with n=5 and output_path=None
    sales_data = task_func(n=5, output_path=None)
    assert sales_data.shape == (5, 3)
    assert sales_data['Country'].dtype == 'object'
    assert sales_data['Product'].dtype == 'object'
    assert sales_data['Sales'].dtype == 'int64'

    # Test case 2: Test with n=10 and output_path='sales_data.csv'
    sales_data = task_func(n=10, output_path='sales_data.csv')
    assert sales_data.shape == (10, 3)
    assert sales_data['Country'].dtype == 'object'
    assert sales_data['Product'].dtype == 'object'
    assert sales_data['Sales'].dtype == 'int64'
    with open('sales_data.csv', 'r') as f:
        lines = f.readlines()
        assert len(lines) == 11  # Header + 10 rows

    # Test case 3: Test with n=5 and random_seed=42
    sales_data_1 = task_func(n=5, random_seed=42)
    sales_data_2 = task_func(n=5, random_seed=42)
    assert sales_data_1.equals(sales_data_2)  # Two calls with the same random_seed should return the same data
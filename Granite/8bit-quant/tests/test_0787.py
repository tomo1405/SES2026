import os

from src_0787 import task_func


def test_task_func():
    # Test case 1: Test with n=5 and random_seed=42
    sales_df = task_func(n=5, random_seed=42)
    assert sales_df.shape == (5, 3)
    assert sales_df['Country'].iloc[0] in ['USA', 'UK', 'China', 'India', 'Germany']
    assert sales_df['Product'].iloc[0] in ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    assert sales_df['Sales'].iloc[0] >= 1 and sales_df['Sales'].iloc[0] <= 100

    # Test case 2: Test with n=10 and output_path='sales_data.csv'
    sales_df = task_func(n=10, output_path='sales_data.csv')
    assert sales_df.shape == (10, 3)
    assert 'sales_data.csv' in os.listdir()

    # Test case 3: Test with n=15 and random_seed=None
    sales_df = task_func(n=15)
    assert sales_df.shape == (15, 3)
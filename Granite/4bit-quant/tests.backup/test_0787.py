import pytest
from src_0787 import task_func

def test_task_func():
    # Test case 1: Test with n=5 and random_seed=42
    sales_df = task_func(n=5, random_seed=42)
    assert sales_df.shape == (5, 3)
    assert sales_df['Country'].iloc[0] in ['USA', 'UK', 'China', 'India', 'Germany']
    assert sales_df['Product'].iloc[0] in ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    assert sales_df['Sales'].iloc[0] >= 1 and sales_df['Sales'].iloc[0] <= 100

    # Test case 2: Test with n=100 and output_path='sales_data.csv'
    task_func(n=100, output_path='sales_data.csv')
    with open('sales_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        assert len(rows) == 100
        assert rows[0] == {'Country': 'USA', 'Product': 'Product A', 'Sales': '1'}

    # Clean up
    import os
    os.remove('sales_data.csv')

if __name__ == '__main__':
    pytest.main()
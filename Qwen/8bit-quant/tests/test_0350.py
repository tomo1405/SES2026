import pytest
from src_0350 import task_func
import pandas as pd

def test_task_func():
    # Test with a small list of products and categories
    product_list = ['Product A', 'Product B']
    categories = ['Category X', 'Category Y']

    # Call the function
    df = task_func(product_list, categories)

    # Check if the DataFrame has the correct columns
    assert all(column in df.columns for column in ['Product', 'Category', 'Quantity Sold', 'Revenue'])

    # Check if the number of rows matches the number of products
    assert len(df) == len(product_list)

    # Check if the values in the 'Product' column match the input list
    assert set(df['Product']) == set(product_list)

    # Check if the 'Category' values are within the provided categories
    assert all(category in categories for category in df['Category'])

    # Check if 'Quantity Sold' and 'Revenue' are integers and within expected ranges
    for index, row in df.iterrows():
        assert isinstance(row['Quantity Sold'], int)
        assert 1 <= row['Quantity Sold'] <= 100
        assert isinstance(row['Revenue'], int)
        assert 10 <= row['Revenue'] / row['Quantity Sold'] <= 100

# Run the tests
if __name__ == "__main__":
    pytest.main()
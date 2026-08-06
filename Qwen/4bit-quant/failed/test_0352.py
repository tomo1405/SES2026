import pytest
from src_0352 import task_func

def test_task_func():
    # Test with a simple list of products and categories
    product_list = ['Product A', 'Product B']
    categories = ['Category 1', 'Category 2']
    
    # Call the function
    df = task_func(product_list, categories)
    
    # Check if the DataFrame has the correct columns
    assert all(column in df.columns for column in ['Product', 'Category', 'Quantity Sold', 'Revenue'])
    
    # Check if the number of rows is equal to the length of the product list
    assert len(df) == len(product_list)
    
    # Check if the values in 'Quantity Sold' and 'Revenue' are within the specified range
    for index, row in df.iterrows():
        assert min_value <= row['Quantity Sold'] <= max_value
        assert min_value <= row['Revenue'] <= max_value

# Additional test cases can be added as needed
import pytest
from src_0350 import task_func

def test_task_func():
    # Define test data
    product_list = ['Product A', 'Product B', 'Product C']
    categories = ['Category 1', 'Category 2', 'Category 3']

    # Call the function
    df = task_func(product_list, categories)

    # Check that the DataFrame has the correct columns
    assert all(column in df.columns for column in ['Product', 'Category', 'Quantity Sold', 'Revenue'])

    # Check that the number of rows in the DataFrame matches the number of products
    assert len(df) == len(product_list)

    # Check that each product is present in the DataFrame
    for product in product_list:
        assert product in df['Product'].values

    # Check that each category is one of the provided categories
    for category in df['Category'].values:
        assert category in categories

    # Check that 'Quantity Sold' and 'Revenue' are within the expected range
    for index, row in df.iterrows():
        assert 1 <= row['Quantity Sold'] <= 100
        assert 10 <= row['Revenue'] / row['Quantity Sold'] <= 100

    # Check that the DataFrame is a pandas DataFrame
    assert isinstance(df, pd.DataFrame)
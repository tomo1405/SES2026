import pytest
from src_0628 import task_func
from statistics import mean
import pandas as pd

def test_task_func():
    # Test with an empty list
    products_list = []
    result_df = task_func(products_list)
    assert result_df.empty, "Expected an empty DataFrame for an empty input list"

    # Test with a list of one product
    products_list = ["Product A"]
    result_df = task_func(products_list)
    assert len(result_df) == 1, "Expected one row in the DataFrame for one product"
    assert len(result_df.columns) == 14, "Expected 14 columns in the DataFrame (1 for product name and 12 for months + 1 for average)"
    
    # Verify the column names
    expected_columns = ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']
    assert list(result_df.columns) == expected_columns, "Column names do not match expected output"

    # Verify the data types
    assert result_df.dtypes['Product'] == object, "Product column should be of type object"
    for month in range(12):
        assert result_df.dtypes[f'Month {month+1}'] == int, f"Month {month+1} column should be of type int"
    assert result_df.dtypes['Average Sales'] == float, "Average Sales column should be of type float"

    # Verify the average sales calculation
    sales_values = result_df.iloc[0][1:13].tolist()
    calculated_avg_sales = mean(sales_values)
    assert calculated_avg_sales == result_df.iloc[0]['Average Sales'], "Calculated average sales does not match the DataFrame value"

    # Test with a list of multiple products
    products_list = ["Product A", "Product B", "Product C"]
    result_df = task_func(products_list)
    assert len(result_df) == 3, "Expected three rows in the DataFrame for three products"
    assert len(result_df.columns) == 14, "Expected 14 columns in the DataFrame (1 for product name and 12 for months + 1 for average)"

    # Verify the data types for multiple products
    assert result_df.dtypes['Product'] == object, "Product column should be of type object"
    for month in range(12):
        assert result_df.dtypes[f'Month {month+1}'] == int, f"Month {month+1} column should be of type int"
    assert result_df.dtypes['Average Sales'] == float, "Average Sales column should be of type float"

    # Verify the average sales calculation for each product
    for index, row in result_df.iterrows():
        sales_values = row[1:13].tolist()
        calculated_avg_sales = mean(sales_values)
        assert calculated_avg_sales == row['Average Sales'], f"Calculated average sales does not match the DataFrame value for product {row['Product']}"

# Run the tests
if __name__ == "__main__":
    pytest.main()
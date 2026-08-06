import pytest
from src_0628 import task_func
from statistics import mean
import pandas as pd

def test_task_func():
    # Test with an empty list
    result = task_func([])
    assert result.empty, "Expected an empty DataFrame for an empty input list"

    # Test with a list of one product
    product_list = ["Product A"]
    result = task_func(product_list)
    assert len(result) == 1, "Expected one row for one product"
    assert all(col in result.columns for col in ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']), "DataFrame columns do not match expected output"

    # Verify data types and calculations
    for index, row in result.iterrows():
        assert row['Product'] == "Product A", "Product name does not match"
        monthly_sales = [row[f'Month {i+1}'] for i in range(12)]
        assert all(isinstance(sale, int) for sale in monthly_sales), "Monthly sales should be integers"
        calculated_avg_sales = mean(monthly_sales)
        assert row['Average Sales'] == calculated_avg_sales, "Average sales calculation is incorrect"

    # Test with a list of multiple products
    product_list = ["Product A", "Product B"]
    result = task_func(product_list)
    assert len(result) == 2, "Expected two rows for two products"
    for index, row in result.iterrows():
        assert row['Product'] in ["Product A", "Product B"], "Product name does not match"
        monthly_sales = [row[f'Month {i+1}'] for i in range(12)]
        assert all(isinstance(sale, int) for sale in monthly_sales), "Monthly sales should be integers"
        calculated_avg_sales = mean(monthly_sales)
        assert row['Average Sales'] == calculated_avg_sales, "Average sales calculation is incorrect"
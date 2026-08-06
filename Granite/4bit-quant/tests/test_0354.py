import pandas as pd
import random
import pytest

from src_0354 import task_func

@pytest.mark.parametrize("product_list, categories, min_value, max_value, expected_columns", [
    (["Product1", "Product2"], ["Category1", "Category2"], 10, 100, ["Product", "Category", "Quantity Sold", "Revenue", "Total Revenue"]),
    (["Product1", "Product2", "Product3"], ["Category1", "Category2", "Category3"], 5, 50, ["Product", "Category", "Quantity Sold", "Revenue", "Total Revenue"]),
    (["Product1", "Product2", "Product3", "Product4"], ["Category1", "Category2", "Category3", "Category4"], 1, 10, ["Product", "Category", "Quantity Sold", "Revenue", "Total Revenue"])
])
def test_task_func(product_list, categories, min_value, max_value, expected_columns):
    report_df = task_func(product_list, categories, min_value, max_value)
    assert report_df.columns.tolist() == expected_columns
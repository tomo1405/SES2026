import pandas as pd
import random
import pytest
from src_0352 import task_func

@pytest.mark.parametrize("product_list, categories, min_value, max_value, expected_columns", [
    (["Product A", "Product B", "Product C"], ["Category 1", "Category 2"], 10, 100, ["Product", "Category", "Quantity Sold", "Revenue"]),
    (["Product X", "Product Y", "Product Z"], ["Category 3", "Category 4"], 5, 50, ["Product", "Category", "Quantity Sold", "Revenue"]),
])
def test_task_func(product_list, categories, min_value, max_value, expected_columns):
    report_df = task_func(product_list, categories, min_value, max_value)
    assert report_df.columns.tolist() == expected_columns
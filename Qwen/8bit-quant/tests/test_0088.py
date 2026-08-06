import pytest
from src_0088 import task_func
import pandas as pd

def test_task_func():
    products = ["ProductA", "ProductB", "ProductC"]
    ratings = [1, 2, 3, 4, 5]
    weights = [0.1, 0.2, 0.3, 0.2, 0.2]

    result_df = task_func(products, ratings, weights)

    # Check if the result is a DataFrame
    assert isinstance(result_df, pd.DataFrame)

    # Check if the DataFrame has the correct columns
    assert list(result_df.columns) == ["Product", "Rating"]

    # Check if the DataFrame is sorted by Rating in descending order
    assert result_df["Rating"].is_monotonic_decreasing

    # Check if the DataFrame contains the correct number of rows
    assert len(result_df) == len(products)

    # Check if the Product column contains the correct values
    assert all(product in result_df["Product"].values for product in products)

    # Check if the Rating column contains values within the specified range
    assert all(1 <= rating <= 5 for rating in result_df["Rating"].values)

def test_task_func_with_empty_products():
    products = []
    ratings = [1, 2, 3, 4, 5]
    weights = [0.1, 0.2, 0.3, 0.2, 0.2]

    result_df = task_func(products, ratings, weights)

    # Check if the result is a DataFrame
    assert isinstance(result_df, pd.DataFrame)

    # Check if the DataFrame is empty
    assert result_df.empty

def test_task_func_with_single_product():
    products = ["ProductA"]
    ratings = [1, 2, 3, 4, 5]
    weights = [0.1, 0.2, 0.3, 0.2, 0.2]

    result_df = task_func(products, ratings, weights)

    # Check if the result is a DataFrame
    assert isinstance(result_df, pd.DataFrame)

    # Check if the DataFrame has the correct columns
    assert list(result_df.columns) == ["Product", "Rating"]

    # Check if the DataFrame is sorted by Rating in descending order
    assert result_df["Rating"].is_monotonic_decreasing

    # Check if the DataFrame contains the correct number of rows
    assert len(result_df) == 1

    # Check if the Product column contains the correct value
    assert result_df["Product"].values[0] == "ProductA"

    # Check if the Rating column contains a value within the specified range
    assert 1 <= result_df["Rating"].values[0] <= 5
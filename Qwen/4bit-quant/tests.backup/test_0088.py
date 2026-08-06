import pytest
from src_0088 import task_func
import pandas as pd

def test_task_func():
    products = ["A", "B", "C"]
    ratings = [1, 2, 3]
    weights = [0.1, 0.3, 0.6]

    # Expected result with fixed seed
    expected_df = pd.DataFrame({
        "Product": ["C", "B", "A"],
        "Rating": [3, 2, 1]
    })

    # Run the function
    result_df = task_func(products, ratings, weights, random_seed=42)

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_empty_products():
    products = []
    ratings = [1, 2, 3]
    weights = [0.1, 0.3, 0.6]

    # Expected result is an empty DataFrame
    expected_df = pd.DataFrame(columns=["Product", "Rating"])

    # Run the function
    result_df = task_func(products, ratings, weights, random_seed=42)

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_single_product():
    products = ["X"]
    ratings = [1, 2, 3]
    weights = [0.1, 0.3, 0.6]

    # Expected result with fixed seed
    expected_df = pd.DataFrame({
        "Product": ["X"],
        "Rating": [3]  # Since weight of 3 is highest
    })

    # Run the function
    result_df = task_func(products, ratings, weights, random_seed=42)

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_different_weights():
    products = ["D", "E", "F"]
    ratings = [1, 2, 3]
    weights = [0.7, 0.2, 0.1]

    # Expected result with fixed seed
    expected_df = pd.DataFrame({
        "Product": ["D", "E", "F"],
        "Rating": [1, 2, 3]
    })

    # Run the function
    result_df = task_func(products, ratings, weights, random_seed=42)

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)
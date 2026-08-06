import pytest
from src_0527 import task_func
import pandas as pd
import numpy as np
from collections import defaultdict

def test_task_func_with_valid_json():
    # Create a temporary JSON file with valid data
    data = [
        {"a": 1, "b": 2},
        {"a": 3, "b": 4},
        {"a": 5}
    ]
    with open("test_data.json", "w") as f:
        json.dump(data, f)

    # Expected output
    expected_df = pd.DataFrame({
        "mean": [3.0, 3.0, np.nan],
        "median": [3.0, 3.0, np.nan]
    }, index=["a", "b"])

    # Run the function
    result_df = task_func("test_data.json")

    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_empty_json():
    # Create a temporary JSON file with empty data
    data = []
    with open("test_data.json", "w") as f:
        json.dump(data, f)

    # Expected output
    expected_df = pd.DataFrame(columns=["mean", "median"]).sort_index()

    # Run the function
    result_df = task_func("test_data.json")

    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_non_numeric_values():
    # Create a temporary JSON file with non-numeric values
    data = [
        {"a": "1", "b": "two"},
        {"a": 3, "b": 4},
        {"a": 5}
    ]
    with open("test_data.json", "w") as f:
        json.dump(data, f)

    # Expected output
    expected_df = pd.DataFrame({
        "mean": [3.0, np.nan, np.nan],
        "median": [3.0, np.nan, np.nan]
    }, index=["a", "b"])

    # Run the function
    result_df = task_func("test_data.json")

    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_missing_keys():
    # Create a temporary JSON file with missing keys
    data = [
        {"a": 1, "b": 2},
        {"a": 3},
        {"b": 4}
    ]
    with open("test_data.json", "w") as f:
        json.dump(data, f)

    # Expected output
    expected_df = pd.DataFrame({
        "mean": [2.0, 3.0],
        "median": [2.0, 3.0]
    }, index=["a", "b"])

    # Run the function
    result_df = task_func("test_data.json")

    # Check if the result matches the expected output
    pd.testing.assert_frame_equal(result_df, expected_df)
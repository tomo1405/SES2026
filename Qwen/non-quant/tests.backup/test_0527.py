import pytest
from src_0527 import task_func
import pandas as pd
import numpy as np
from collections import defaultdict

def test_task_func_with_default_input():
    # Prepare a sample JSON file with known data
    sample_data = [
        {"a": 1, "b": 2},
        {"a": 3, "b": 4, "c": 5},
        {"a": 6, "b": np.nan}
    ]
    with open("test_data.json", "w") as f:
        json.dump(sample_data, f)

    # Expected result
    expected_stats = {
        "a": [1, 3, 6],
        "b": [2, 4, np.nan],
        "c": [np.nan, 5, np.nan]
    }
    expected_result = {
        "a": {"mean": 3.6666666666666665, "median": 3.0},
        "b": {"mean": 3.0, "median": 3.0},
        "c": {"mean": 5.0, "median": 5.0}
    }
    expected_df = pd.DataFrame(expected_result).transpose().sort_index()

    # Run the function
    result_df = task_func("test_data.json")

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_empty_input():
    # Prepare an empty JSON file
    with open("empty_data.json", "w") as f:
        json.dump([], f)

    # Expected result is an empty DataFrame
    expected_df = pd.DataFrame(columns=["mean", "median"]).sort_index()

    # Run the function
    result_df = task_func("empty_data.json")

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.json")
import pytest
from src_0887 import task_func
import pandas as pd
from collections import Counter

def test_task_func():
    # Test case 1: Basic functionality
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Age': [25, 30, 25, 30],
        'Score': [85, 90, 88, 92]
    }
    expected_df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
        'Age': [25, 30, 25, 30],
        'Score': [85, 90, 88, 92]
    })
    expected_df_sorted = expected_df.sort_values(['Name', 'Age'])
    expected_avg_scores = expected_df.groupby('Name')['Score'].mean()
    expected_most_common_age = 27  # Average of 25, 30

    result_df, result_avg_scores, result_most_common_age = task_func(data)

    pd.testing.assert_frame_equal(result_df, expected_df_sorted)
    pd.testing.assert_series_equal(result_avg_scores, expected_avg_scores)
    assert result_most_common_age == expected_most_common_age

    # Add more test cases as needed

    # Add more test cases to cover different scenarios
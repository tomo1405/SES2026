import pandas as pd
import pytest
from src_0887 import task_func


def test_task_func_valid_data():
    data = {
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
        'Age': [25, 30, 25, 35],
        'Score': [88, 92, 85, 90]
    }
    df, avg_scores, most_common_age = task_func(data)
    
    # Check DataFrame
    expected_df = pd.DataFrame({
        'Name': ['Alice', 'Alice', 'Bob', 'Charlie'],
        'Age': [25, 25, 30, 35],
        'Score': [88, 85, 92, 90]
    })
    pd.testing.assert_frame_equal(df.sort_values(['Name', 'Age']).reset_index(drop=True), expected_df.reset_index(drop=True))
    
    # Check Average Scores
    expected_avg_scores = pd.Series({'Alice': 86.5, 'Bob': 92.0, 'Charlie': 90.0})
    pd.testing.assert_series_equal(avg_scores.sort_index(), expected_avg_scores.sort_index())
    
    # Check Most Common Age
    assert most_common_age == 25

def test_task_func_missing_keys():
    data = {
        'Name': ['Alice', 'Bob'],
        'Age': [25, 30]
    }
    with pytest.raises(ValueError) as excinfo:
        task_func(data)
    assert "The dictionary must have the keys 'Name', 'Age', 'Score'" in str(excinfo.value)

def test_task_func_empty_data():
    data = {
        'Name': [],
        'Age': [],
        'Score': []
    }
    df, avg_scores, most_common_age = task_func(data)
    
    # Check DataFrame
    expected_df = pd.DataFrame(columns=['Name', 'Age', 'Score'])
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check Average Scores
    expected_avg_scores = pd.Series(dtype=float)
    pd.testing.assert_series_equal(avg_scores, expected_avg_scores)
    
    # Check Most Common Age
    assert most_common_age is None

def test_task_func_single_entry():
    data = {
        'Name': ['Alice'],
        'Age': [25],
        'Score': [88]
    }
    df, avg_scores, most_common_age = task_func(data)
    
    # Check DataFrame
    expected_df = pd.DataFrame({
        'Name': ['Alice'],
        'Age': [25],
        'Score': [88]
    })
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check Average Scores
    expected_avg_scores = pd.Series({'Alice': 88.0})
    pd.testing.assert_series_equal(avg_scores, expected_avg_scores)
    
    # Check Most Common Age
    assert most_common_age == 25
import pytest
from src_0887 import task_func
import pandas as pd

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
    pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df)
    
    # Check average scores
    expected_avg_scores = pd.Series([86.5, 92, 90], index=['Alice', 'Bob', 'Charlie'])
    pd.testing.assert_series_equal(avg_scores, expected_avg_scores)
    
    # Check most common age
    assert most_common_age == 25

def test_task_func_missing_key():
    data = {
        'Name': ['Alice', 'Bob'],
        'Age': [25, 30]
    }
    with pytest.raises(ValueError, match="The dictionary must have the keys 'Name', 'Age', 'Score'"):
        task_func(data)

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
    
    # Check average scores
    expected_avg_scores = pd.Series(dtype=float)
    pd.testing.assert_series_equal(avg_scores, expected_avg_scores)
    
    # Check most common age
    assert most_common_age is None
import pytest
from src_0532 import task_func
import pandas as pd
import numpy as np
from collections import Counter

@pytest.fixture
def sample_data():
    data = {
        "x": [1, 2, 2, 3, 4, 4, 5],
        "y": [1, 2, 2, 3, 4, 4, 5]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    duplicates_counter, unique_df, ax = task_func(sample_data, n_clusters=3, random_state=0, n_init=10)
    
    # Check duplicates counter
    expected_duplicates_counter = Counter({(2, 2): 2, (4, 4): 2})
    assert duplicates_counter == expected_duplicates_counter
    
    # Check unique DataFrame
    expected_unique_data = {
        "x": [1, 2, 3, 4, 5],
        "y": [1, 2, 3, 4, 5]
    }
    expected_unique_df = pd.DataFrame(expected_unique_data)
    pd.testing.assert_frame_equal(unique_df[["x", "y"]], expected_unique_df)
    
    # Check cluster column exists and has correct number of unique values
    assert "cluster" in unique_df.columns
    assert unique_df["cluster"].nunique() <= 3

def test_task_func_no_duplicates():
    data = {
        "x": [1, 2, 3, 4, 5],
        "y": [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=3, random_state=0, n_init=10)
    
    # Check duplicates counter
    expected_duplicates_counter = Counter()
    assert duplicates_counter == expected_duplicates_counter
    
    # Check unique DataFrame
    pd.testing.assert_frame_equal(unique_df, df)
    
    # Check cluster column exists and has correct number of unique values
    assert "cluster" in unique_df.columns
    assert unique_df["cluster"].nunique() <= 3

def test_task_func_fewer_unique_points_than_clusters():
    data = {
        "x": [1, 1, 2, 2],
        "y": [1, 1, 2, 2]
    }
    df = pd.DataFrame(data)
    duplicates_counter, unique_df, ax = task_func(df, n_clusters=5, random_state=0, n_init=10)
    
    # Check duplicates counter
    expected_duplicates_counter = Counter({(1, 1): 2, (2, 2): 2})
    assert duplicates_counter == expected_duplicates_counter
    
    # Check unique DataFrame
    expected_unique_data = {
        "x": [1, 2],
        "y": [1, 2]
    }
    expected_unique_df = pd.DataFrame(expected_unique_data)
    pd.testing.assert_frame_equal(unique_df[["x", "y"]], expected_unique_df)
    
    # Check cluster column exists and has correct number of unique values
    assert "cluster" in unique_df.columns
    assert unique_df["cluster"].nunique() == 2
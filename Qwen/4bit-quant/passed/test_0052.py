import pytest
from src_0052 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        "Age": [25, 30, 35, 40, 45, 50],
        "Height": [160, 170, 180, 190, 200, 210]
    }
    return pd.DataFrame(data)

def test_task_func_no_clusters(sample_data):
    age_threshold = 40
    height_threshold = 180
    result_df, ax = task_func(sample_data, age_threshold, height_threshold)
    assert ax is None
    assert all(result_df["Cluster"] == 0)

def test_task_func_with_clusters(sample_data):
    age_threshold = 30
    height_threshold = 200
    result_df, ax = task_func(sample_data, age_threshold, height_threshold)
    assert ax is not None
    assert len(result_df) == 3
    assert all(result_df["Cluster"].isin([0, 1, 2]))

def test_task_func_empty_result(sample_data):
    age_threshold = 55
    height_threshold = 150
    result_df, ax = task_func(sample_data, age_threshold, height_threshold)
    assert ax is None
    assert result_df.empty

def test_task_func_single_row(sample_data):
    age_threshold = 30
    height_threshold = 170
    result_df, ax = task_func(sample_data, age_threshold, height_threshold)
    assert ax is None
    assert len(result_df) == 1
    assert all(result_df["Cluster"] == 0)

def test_task_func_two_rows(sample_data):
    age_threshold = 35
    height_threshold = 190
    result_df, ax = task_func(sample_data, age_threshold, height_threshold)
    assert ax is None
    assert len(result_df) == 2
    assert all(result_df["Cluster"] == 0)
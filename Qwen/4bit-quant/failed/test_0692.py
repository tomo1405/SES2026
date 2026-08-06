import pytest
from src_0692 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_data():
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1]
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    labels = task_func(sample_data)
    assert isinstance(labels, np.ndarray), "The output should be a numpy array"
    assert len(labels) == len(sample_data), "The length of labels should match the number of rows in the input DataFrame"
    assert labels.min() >= 0 and labels.max() <= 2, "Labels should be within the range of 0 to 2"

def test_task_func_with_empty_data():
    empty_df = pd.DataFrame(columns=['feature1', 'feature2'])
    labels = task_func(empty_df)
    assert isinstance(labels, np.ndarray), "The output should be a numpy array"
    assert len(labels) == 0, "The length of labels should be 0 for an empty DataFrame"

def test_task_func_with_single_row_data():
    single_row_df = pd.DataFrame({
        'feature1': [1],
        'feature2': [1]
    })
    labels = task_func(single_row_df)
    assert isinstance(labels, np.ndarray), "The output should be a numpy array"
    assert len(labels) == 1, "The length of labels should match the number of rows in the input DataFrame"
    assert labels[0] == 0, "For a single row, the label should be 0"

def test_task_func_with_single_column_data():
    single_column_df = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5]
    })
    labels = task_func(single_column_df)
    assert isinstance(labels, np.ndarray), "The output should be a numpy array"
    assert len(labels) == len(single_column_df), "The length of labels should match the number of rows in the input DataFrame"
    assert labels.min() >= 0 and labels.max() <= 2, "Labels should be within the range of 0 to 2"
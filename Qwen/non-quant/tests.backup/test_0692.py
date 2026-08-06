import pytest
from src_0692 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'feature1': [1.0, 2.0, 3.0, 4.0],
        'feature2': [5.0, 6.0, 7.0, 8.0]
    }
    return pd.DataFrame(data)

def test_task_func_output_type(sample_df):
    labels = task_func(sample_df)
    assert isinstance(labels, np.ndarray), "The output should be a numpy array."

def test_task_func_output_length(sample_df):
    labels = task_func(sample_df)
    assert len(labels) == sample_df.shape[0], "The number of labels should match the number of rows in the input DataFrame."

def test_task_func_output_values(sample_df):
    labels = task_func(sample_df)
    assert all(label in range(3) for label in labels), "All labels should be in the range 0 to 2."

def test_task_func_with_empty_df():
    empty_df = pd.DataFrame(columns=['feature1', 'feature2'])
    labels = task_func(empty_df)
    assert len(labels) == 0, "The output should be an empty array for an empty input DataFrame."

def test_task_func_with_single_row_df():
    single_row_df = pd.DataFrame({'feature1': [1.0], 'feature2': [5.0]})
    labels = task_func(single_row_df)
    assert len(labels) == 1, "The output should have one label for a single row input DataFrame."
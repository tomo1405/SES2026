import pytest
from src_0036 import task_func
import pandas as pd
import numpy as np

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [3, 4, 5, 6, 7],
        'C': [4, 5, 6, 7, 8]
    }
    return pd.DataFrame(data)

def test_task_func_output(sample_df):
    modified_df, ax = task_func(sample_df)
    expected_data = {
        'A': [1, 0, 3, 4, 0],
        'B': [0, 0, 3, 4, 0],
        'C': [4, 0, 0, 0, 0]
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(modified_df, expected_df)

def test_task_func_plot(sample_df, mocker):
    mock_kdeplot = mocker.patch('seaborn.kdeplot')
    mock_gca = mocker.patch('matplotlib.pyplot.gca')
    
    task_func(sample_df)
    
    assert mock_kdeplot.call_count == 3  # One call per column
    assert mock_gca.called

def test_task_func_default_target_values(sample_df):
    modified_df, _ = task_func(sample_df)
    expected_data = {
        'A': [1, 0, 3, 4, 0],
        'B': [0, 0, 3, 4, 0],
        'C': [4, 0, 0, 0, 0]
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(modified_df, expected_df)

def test_task_func_custom_target_values(sample_df):
    modified_df, _ = task_func(sample_df, target_values=[2, 5])
    expected_data = {
        'A': [0, 2, 0, 0, 5],
        'B': [0, 0, 0, 0, 0],
        'C': [0, 0, 0, 0, 0]
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(modified_df, expected_df)
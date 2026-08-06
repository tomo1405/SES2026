import pytest
from src_0036 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    
    # Check if the modified DataFrame contains only the target values and zeros
    expected_data = {
        'A': [1, 0, 3, 4, 0],
        'B': [0, 0, 3, 4, 0],
        'C': [0, 0, 0, 4, 0]
    }
    expected_df = pd.DataFrame(expected_data)
    assert modified_df.equals(expected_df), "The modified DataFrame does not match the expected output."
    
    # Check if the plot is created with the correct number of subplots
    assert len(ax.lines) == 3, "The plot should have 3 lines (one for each column)."

def test_task_func_with_custom_target_values(sample_df):
    modified_df, ax = task_func(sample_df, target_values=[2, 5, 8])
    
    # Check if the modified DataFrame contains only the custom target values and zeros
    expected_data = {
        'A': [0, 2, 0, 0, 5],
        'B': [0, 0, 0, 0, 0],
        'C': [0, 0, 0, 0, 8]
    }
    expected_df = pd.DataFrame(expected_data)
    assert modified_df.equals(expected_df), "The modified DataFrame does not match the expected output with custom target values."

def test_task_func_no_target_values(sample_df):
    modified_df, ax = task_func(sample_df, target_values=[])
    
    # Check if the modified DataFrame contains only zeros
    expected_data = {
        'A': [0, 0, 0, 0, 0],
        'B': [0, 0, 0, 0, 0],
        'C': [0, 0, 0, 0, 0]
    }
    expected_df = pd.DataFrame(expected_data)
    assert modified_df.equals(expected_df), "The modified DataFrame should contain only zeros when no target values are provided."
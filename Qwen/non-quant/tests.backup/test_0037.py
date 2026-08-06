import pytest
from src_0037 import task_func
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    return pd.DataFrame(data)

def test_task_func_positive_values(sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df)

def test_task_func_constant_column():
    data = {
        'A': [1, 1, 1],
        'B': [2, 2, 2],
        'C': [3, 3, 3]
    }
    df = pd.DataFrame(data)
    transformed_df, fig = task_func(df)
    assert transformed_df.equals(df)
    plt.close(fig)

def test_task_func_non_constant_column():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    df = pd.DataFrame(data)
    transformed_df, fig = task_func(df)
    assert transformed_df.shape == df.shape
    plt.close(fig)

def test_task_func_with_target_values():
    data = {
        'A': [1, 3, 4],
        'B': [2, 5, 6],
        'C': [7, 8, 9]
    }
    df = pd.DataFrame(data)
    transformed_df, fig = task_func(df)
    expected_data = {
        'A': [1, 3, 4],
        'B': [0, 0, 0],
        'C': [0, 0, 0]
    }
    expected_df = pd.DataFrame(expected_data)
    assert transformed_df.equals(expected_df)
    plt.close(fig)
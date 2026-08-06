import pytest
from src_0239 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'Score': [88, 92, 87, 88]
    }
    return pd.DataFrame(data)

def test_task_func_duplicates(sample_df):
    df, ax = task_func(sample_df)
    assert len(df) == 3, "Duplicate names should be removed"
    assert 'Name' not in df.duplicated().any(), "Duplicates should be removed based on 'Name' column"

def test_task_func_standardization(sample_df):
    df, ax = task_func(sample_df)
    assert np.allclose(df['Age'].mean(), 0, atol=1e-7), "Age should be standardized with mean 0"
    assert np.allclose(df['Score'].mean(), 0, atol=1e-7), "Score should be standardized with mean 0"

def test_task_func_plot(sample_df):
    df, ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes), "Function should return a matplotlib Axes object"
    assert ax.get_xlabel() == 'Age (standardized)', "X-axis label should be 'Age (standardized)'"
    assert ax.get_ylabel() == 'Score (standardized)', "Y-axis label should be 'Score (standardized)'"
    assert ax.get_title() == 'Scatter Plot of Standardized Age and Score', "Plot title should be correct"

def test_task_func_no_change_to_original_df(sample_df):
    original_df = sample_df.copy()
    df, ax = task_func(sample_df)
    assert sample_df.equals(original_df), "Original DataFrame should not be modified"
import pytest
from src_0239 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_df():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David'],
        'Age': [25, 30, 35, 25, 40],
        'Score': [88, 92, 87, 88, 95]
    }
    return pd.DataFrame(data)

def test_task_func_drops_duplicates(sample_df):
    df, _ = task_func(sample_df)
    assert df.shape[0] == 4, "Duplicate names were not dropped correctly."

def test_task_func_standardizes_columns(sample_df):
    df, _ = task_func(sample_df)
    assert np.allclose(df['Age'].mean(), 0, atol=1e-7), "Age column was not standardized."
    assert np.allclose(df['Score'].mean(), 0, atol=1e-7), "Score column was not standardized."

def test_task_func_returns_correct_shape(sample_df):
    df, _ = task_func(sample_df)
    assert df.shape == (4, 3), "The DataFrame shape is incorrect after processing."

def test_task_func_creates_scatter_plot(sample_df):
    _, ax = task_func(sample_df)
    assert isinstance(ax, plt.Axes), "The function did not return a matplotlib Axes object."
    assert ax.get_xlabel() == 'Age (standardized)', "X-axis label is incorrect."
    assert ax.get_ylabel() == 'Score (standardized)', "Y-axis label is incorrect."
    assert ax.get_title() == 'Scatter Plot of Standardized Age and Score', "Plot title is incorrect."
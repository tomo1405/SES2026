import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0983 import task_func


@pytest.fixture
def sample_df():
    data = {
        'A': np.random.normal(loc=0, scale=1, size=100),
        'B': np.random.normal(loc=5, scale=2, size=100)
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    ax = task_func(sample_df, 'A')
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object."

def test_task_func_with_seed(sample_df):
    ax1 = task_func(sample_df, 'A', seed=42)
    ax2 = task_func(sample_df, 'A', seed=42)
    assert ax1 == ax2, "With the same seed, the function should produce the same plot."

def test_task_func_non_default_bins(sample_df):
    ax = task_func(sample_df, 'A', bins=20)
    assert len(ax.patches) == 20, "The number of bins should match the specified value."

def test_task_func_non_default_density(sample_df):
    ax = task_func(sample_df, 'A', density=False)
    assert not ax.get_yaxis().get_label_text() == "Density", "Y-axis label should not be 'Density' when density is False."

def test_task_func_non_default_color(sample_df):
    ax = task_func(sample_df, 'A', color='r')
    assert ax.patches[0].get_facecolor() == (1.0, 0.0, 0.0, 0.6), "The color of the histogram should match the specified value."

def test_task_func_non_default_alpha(sample_df):
    ax = task_func(sample_df, 'A', alpha=0.8)
    assert ax.patches[0].get_alpha() == 0.8, "The alpha value of the histogram should match the specified value."

def test_task_func_with_different_column(sample_df):
    ax = task_func(sample_df, 'B')
    assert ax.get_xlabel() == 'B', "The x-axis label should match the specified column name."
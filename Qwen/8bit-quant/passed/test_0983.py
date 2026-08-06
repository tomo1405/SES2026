import pytest
from src_0983 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

@pytest.fixture
def sample_df():
    data = {
        'A': np.random.normal(loc=0, scale=1, size=100),
        'B': np.random.exponential(scale=1.0, size=100)
    }
    return pd.DataFrame(data)

def test_task_func_returns_axes_object(sample_df):
    ax = task_func(sample_df, 'A')
    assert isinstance(ax, plt.Axes)

def test_task_func_sets_correct_title(sample_df):
    ax = task_func(sample_df, 'A')
    assert ax.get_title() == "Normal Fit for 'A'"

def test_task_func_sets_correct_labels(sample_df):
    ax = task_func(sample_df, 'A')
    assert ax.get_ylabel() == "Density"
    assert ax.get_xlabel() == 'A'

def test_task_func_histogram_properties(sample_df):
    ax = task_func(sample_df, 'A', bins=20, density=False, alpha=0.8, color="b")
    lines = ax.get_lines()
    assert len(lines) == 1  # Only the normal fit line should be present
    assert len(ax.patches) == 20  # 20 bins in the histogram

def test_task_func_normal_fit(sample_df):
    ax = task_func(sample_df, 'A')
    lines = ax.get_lines()
    x_data, y_data = lines[0].get_data()
    mu, std = norm.fit(sample_df['A'])
    fitted_y_data = norm.pdf(x_data, mu, std)
    assert np.allclose(y_data, fitted_y_data)

def test_task_func_seed(sample_df):
    ax1 = task_func(sample_df, 'A', seed=42)
    ax2 = task_func(sample_df, 'A', seed=42)
    assert np.array_equal([line.get_xdata() for line in ax1.get_lines()], [line.get_xdata() for line in ax2.get_lines()])
    assert np.array_equal([line.get_ydata() for line in ax1.get_lines()], [line.get_ydata() for line in ax2.get_lines()])
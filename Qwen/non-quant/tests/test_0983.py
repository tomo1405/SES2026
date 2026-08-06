import pytest
from src_0983 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

@pytest.fixture
def sample_df():
    data = {'values': np.random.normal(loc=0, scale=1, size=100)}
    return pd.DataFrame(data)

def test_task_func_output_type(sample_df):
    ax = task_func(sample_df, 'values')
    assert isinstance(ax, plt.Axes)

def test_task_func_histogram_properties(sample_df):
    ax = task_func(sample_df, 'values', bins=10, density=True, alpha=0.5, color="b")
    lines, patches = ax.get_legend_handles_labels()
    assert len(patches) == 10  # Check number of bins
    assert patches[0].get_alpha() == 0.5
    assert patches[0].get_facecolor() == (0, 0, 1, 1)  # Blue color

def test_task_func_normal_fit(sample_df):
    ax = task_func(sample_df, 'values')
    lines, _ = ax.get_legend_handles_labels()
    assert len(lines) == 1  # Only one line for the normal fit
    xdata, ydata = lines[0].get_data()
    mu, std = norm.fit(sample_df['values'])
    fitted_ydata = norm.pdf(xdata, mu, std)
    assert np.allclose(ydata, fitted_ydata)

def test_task_func_title_and_labels(sample_df):
    ax = task_func(sample_df, 'values')
    assert ax.get_title() == "Normal Fit for 'values'"
    assert ax.get_ylabel() == "Density"
    assert ax.get_xlabel() == "values"

def test_task_func_seed(sample_df):
    ax1 = task_func(sample_df, 'values', seed=42)
    ax2 = task_func(sample_df, 'values', seed=42)
    lines1, _ = ax1.get_legend_handles_labels()
    lines2, _ = ax2.get_legend_handles_labels()
    assert np.array_equal(lines1[0].get_xdata(), lines2[0].get_xdata())
    assert np.array_equal(lines1[0].get_ydata(), lines2[0].get_ydata())

def test_task_func_no_seed(sample_df):
    ax1 = task_func(sample_df, 'values')
    ax2 = task_func(sample_df, 'values')
    lines1, _ = ax1.get_legend_handles_labels()
    lines2, _ = ax2.get_legend_handles_labels()
    assert not np.array_equal(lines1[0].get_xdata(), lines2[0].get_xdata())
    assert not np.array_equal(lines1[0].get_ydata(), lines2[0].get_ydata())
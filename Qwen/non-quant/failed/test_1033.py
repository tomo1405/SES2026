import pytest
from src_1033 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def test_task_func_empty_dataframe():
    with pytest.raises(ValueError) as excinfo:
        task_func(rows=0)
    assert "No data to generate heatmap." in str(excinfo.value)

def test_task_func_output_type():
    ax = task_func(rows=10, string_length=3)
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_correlation_matrix_shape():
    ax = task_func(rows=10, string_length=3)
    corr = ax.data
    assert corr.shape == (3, 3)

def test_task_func_correlation_matrix_values():
    ax = task_func(rows=10, string_length=3)
    corr = ax.data
    assert np.allclose(corr.values, corr.values.T)  # Check if the matrix is symmetric

def test_task_func_no_plot_display():
    ax = task_func(rows=10, string_length=3)
    assert plt.fignum_exists(1) is False  # Ensure the plot is closed

def test_task_func_with_different_string_length():
    ax = task_func(rows=10, string_length=5)
    corr = ax.data
    assert corr.shape == (5, 5)

def test_task_func_with_larger_rows():
    ax = task_func(rows=100, string_length=3)
    corr = ax.data
    assert corr.shape == (3, 3)
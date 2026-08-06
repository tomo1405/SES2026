import pytest
import numpy as np
from src_0043 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    np.random.seed(0)
    return np.random.rand(100, 5)

def test_task_func_output(sample_data):
    df, ax = task_func(sample_data, n_components=2)
    
    # Check DataFrame shape
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (100, 3)  # 2 components + 1 mean column
    
    # Check DataFrame columns
    expected_columns = ['Component 1', 'Component 2', 'Mean']
    assert list(df.columns) == expected_columns
    
    # Check plot object
    assert isinstance(ax, plt.Axes)
    
    # Check cumulative explained variance plot
    x_data = np.arange(1, 3)  # Since n_components=2
    y_data = ax.lines[0].get_ydata()
    assert len(y_data) == 2
    assert np.allclose(y_data, [0.486479, 0.978335], atol=1e-5)

def test_task_func_n_components(sample_data):
    df, ax = task_func(sample_data, n_components=3)
    
    # Check DataFrame shape
    assert df.shape == (100, 4)  # 3 components + 1 mean column
    
    # Check DataFrame columns
    expected_columns = ['Component 1', 'Component 2', 'Component 3', 'Mean']
    assert list(df.columns) == expected_columns
    
    # Check plot object
    assert isinstance(ax, plt.Axes)
    
    # Check cumulative explained variance plot
    x_data = np.arange(1, 4)  # Since n_components=3
    y_data = ax.lines[0].get_ydata()
    assert len(y_data) == 3
    assert np.allclose(y_data, [0.486479, 0.978335, 0.999999], atol=1e-5)
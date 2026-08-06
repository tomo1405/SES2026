import pytest
from src_0158 import task_func
import numpy as np
import pandas as pd
import seaborn as sns

@pytest.fixture
def sample_data():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_task_func_input_type(sample_data):
    with pytest.raises(ValueError, match="Input data must be a 2D numpy array."):
        task_func([1, 2, 3])

def test_task_func_input_ndim(sample_data):
    with pytest.raises(ValueError, match="Input data must be a 2D numpy array."):
        task_func(np.array([1, 2, 3]))

def test_task_func_output_type(sample_data):
    df, ax = task_func(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.AxesGrid)

def test_task_func_average_column(sample_data):
    df, _ = task_func(sample_data)
    expected_average = np.array([2, 5, 8])
    assert np.allclose(df['Average'], expected_average)

def test_task_func_correlation_matrix(sample_data):
    df, _ = task_func(sample_data)
    correlation = df.corr()
    expected_correlation = pd.DataFrame({
        0: [1.0, 1.0, 1.0],
        1: [1.0, 1.0, 1.0],
        2: [1.0, 1.0, 1.0],
        'Average': [1.0, 1.0, 1.0]
    })
    assert correlation.equals(expected_correlation)
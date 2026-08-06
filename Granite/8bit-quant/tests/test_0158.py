import numpy as np
import pandas as pd
import pytest
import seaborn as sns
from src_0158 import task_func


@pytest.fixture
def input_data():
    return np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def test_input_type(input_data):
    with pytest.raises(ValueError) as excinfo:
        task_func(input_data)
    assert "Input data must be a 2D numpy array." in str(excinfo.value)

def test_input_ndim(input_data):
    input_data_1d = input_data.reshape(-1)
    with pytest.raises(ValueError) as excinfo:
        task_func(input_data_1d)
    assert "Input data must be a 2D numpy array." in str(excinfo.value)

def test_output_type(input_data):
    df, ax = task_func(input_data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.Axes)

def test_correlation_matrix(input_data):
    df, ax = task_func(input_data)
    correlation = df.corr()
    assert isinstance(correlation, pd.DataFrame)

def test_heatmap(input_data):
    df, ax = task_func(input_data)
    assert isinstance(ax, sns.axisgrid.Axes)

def test_average_column(input_data):
    df, ax = task_func(input_data)
    assert 'Average' in df.columns
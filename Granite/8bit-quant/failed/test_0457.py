import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from src_0457 import task_func
import pytest

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

def test_task_func(sample_data):
    normalized_data, ax = task_func(sample_data)
    assert isinstance(normalized_data, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_task_func_shape(sample_data):
    normalized_data, _ = task_func(sample_data)
    assert normalized_data.shape == sample_data.shape

def test_task_func_columns(sample_data):
    normalized_data, _ = task_func(sample_data)
    assert normalized_data.columns.tolist() == sample_data.columns.tolist()

def test_task_func_normalized_values(sample_data):
    normalized_data, _ = task_func(sample_data)
    scaler = MinMaxScaler()
    expected_values = scaler.fit_transform(sample_data)
    assert (normalized_data == expected_values).all().all()

def test_task_func_heatmap(sample_data):
    _, ax = task_func(sample_data)
    assert ax.get_xlabel() == 'Normalized Value'
    assert ax.get_ylabel() == ''
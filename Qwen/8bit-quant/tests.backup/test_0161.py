import pytest
from src_0161 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return np.random.rand(30, 8)

def test_task_func_column_count(sample_data):
    with pytest.raises(ValueError):
        task_func(np.random.rand(30, 7))

def test_task_func_dataframe_creation(sample_data):
    df, _, _ = task_func(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']

def test_task_func_average_calculation(sample_data):
    df, _, _ = task_func(sample_data)
    expected_average = sample_data.mean(axis=1)
    assert np.allclose(df['Average'].values, expected_average)

def test_task_func_kdeplot_creation(sample_data):
    _, ax, _ = task_func(sample_data)
    assert isinstance(ax, plt.Axes)

def test_task_func_normaltest(sample_data):
    df, _, p = task_func(sample_data)
    if len(df['Average']) >= 20:
        assert p is not None
    else:
        assert p is None

def test_task_func_with_few_samples():
    small_sample_data = np.random.rand(15, 8)
    _, _, p = task_func(small_sample_data)
    assert p is None
import pytest
from src_1025 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1]
    }

@pytest.fixture
def empty_data():
    return {}

@pytest.fixture
def single_value_data():
    return {
        'A': [1, 1, 1, 1, 1]
    }

def test_task_func_with_valid_data(sample_data):
    df, plot = task_func(sample_data)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(plot, plt.AxesSubplot)
    assert plot.get_title() == "Value Distribution"

def test_task_func_with_empty_data(empty_data):
    df, plot = task_func(empty_data)
    assert df.empty
    assert plot is None

def test_task_func_with_single_value_data(single_value_data):
    df, plot = task_func(single_value_data)
    assert df.empty
    assert plot is None

def test_task_func_with_large_data():
    large_data = {f'Col{i}': np.random.rand(1000) for i in range(10)}
    df, plot = task_func(large_data)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert isinstance(plot, plt.AxesSubplot)
    assert plot.get_title() == "Value Distribution"
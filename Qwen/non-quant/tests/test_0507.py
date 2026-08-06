import pytest
from src_0507 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [
        [pd.Timestamp("2023-01-01"), 22, 60, 10, 0],
        [pd.Timestamp("2023-01-02"), 24, 55, 12, 0.1],
        [pd.Timestamp("2023-01-03"), 21, 65, 9, 0],
        [pd.Timestamp("2023-01-04"), 23, 70, 11, 0.2],
        [pd.Timestamp("2023-01-05"), 25, 68, 13, 0]
    ]

def test_task_func_sum(sample_data):
    result = task_func("Temperature", sample_data)
    assert result["sum"] == 115

def test_task_func_mean(sample_data):
    result = task_func("Temperature", sample_data)
    assert np.isclose(result["mean"], 23)

def test_task_func_min(sample_data):
    result = task_func("Temperature", sample_data)
    assert result["min"] == 21

def test_task_func_max(sample_data):
    result = task_func("Temperature", sample_data)
    assert result["max"] == 25

def test_task_func_empty_data():
    empty_data = []
    result = task_func("Temperature", empty_data)
    assert result["sum"] == 0
    assert result["mean"] is np.nan
    assert result["min"] == np.inf
    assert result["max"] == -np.inf

def test_task_func_plot(sample_data):
    result = task_func("Temperature", sample_data)
    assert isinstance(result["plot"], plt.Axes)

def test_task_func_invalid_column(sample_data):
    with pytest.raises(KeyError):
        task_func("InvalidColumn", sample_data)
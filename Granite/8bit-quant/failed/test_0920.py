import pandas as pd
import matplotlib.pyplot as plt
import pytest

from src_0920 import task_func

@pytest.fixture
def sample_data():
    return {'column': ['A', 'B', 'C', 'A', 'B', 'C', 'D', 'E', 'A', 'B']}

def test_task_func(sample_data):
    ax = task_func(sample_data, 'column')
    assert ax is not None
    assert isinstance(ax, plt.Axes)

def test_task_func_invalid_column(sample_data):
    with pytest.raises(KeyError):
        task_func(sample_data, 'invalid_column')

def test_task_func_invalid_data(sample_data):
    with pytest.raises(TypeError):
        task_func('invalid_data', 'column')
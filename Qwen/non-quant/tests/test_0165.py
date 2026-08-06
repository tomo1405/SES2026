import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0165 import task_func


def test_task_func_default_parameters():
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    data = pd.DataFrame(np.random.uniform(0, 1, size=(5, 5)), columns=[f'Label{i + 1}' for i in range(5)])
    assert np.allclose(fig.axes[0].lines[0].get_ydata(), data.sum(axis=1))

def test_task_func_custom_parameters():
    fig = task_func(num_labels=3, data_range=(10, 20))
    assert isinstance(fig, plt.Figure)
    data = pd.DataFrame(np.random.uniform(10, 20, size=(3, 3)), columns=[f'Label{i + 1}' for i in range(3)])
    assert np.allclose(fig.axes[0].lines[0].get_ydata(), data.sum(axis=1))

def test_task_func_zero_labels():
    with pytest.raises(ValueError):
        task_func(num_labels=0)

def test_task_func_negative_labels():
    with pytest.raises(ValueError):
        task_func(num_labels=-1)

def test_task_func_invalid_data_range():
    with pytest.raises(ValueError):
        task_func(data_range=(20, 10))

def test_task_func_single_label():
    fig = task_func(num_labels=1)
    assert isinstance(fig, plt.Figure)
    data = pd.DataFrame(np.random.uniform(0, 1, size=(1, 1)), columns=['Label1'])
    assert np.allclose(fig.axes[0].lines[0].get_ydata(), data.sum(axis=1))
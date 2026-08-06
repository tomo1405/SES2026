import pytest
from src_0393 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Mocking the plt.subplots function to capture the Axes object
class MockAxes:
    def __init__(self):
        self.xlabel_called_with = None
        self.ylabel_called_with = None
        self.title_called_with = None
        self.xticks_called_with = None
        self.bar_called_with = None

    def set_xlabel(self, label):
        self.xlabel_called_with = label

    def set_ylabel(self, label):
        self.ylabel_called_with = label

    def set_title(self, title):
        self.title_called_with = title

    def set_xticks(self, ticks):
        self.xticks_called_with = ticks

    def bar(self, x, height, width, color):
        self.bar_called_with = (x, height, width, color)

def mock_subplots():
    return plt.figure(), MockAxes()

@pytest.fixture
def mock_plt(monkeypatch):
    monkeypatch.setattr(plt, 'subplots', mock_subplots)

@pytest.fixture
def sample_df():
    data = {
        'category': ['A', 'B', 'A', 'C'],
        'values': [10, 20, 30, 40]
    }
    return pd.DataFrame(data)

def test_task_func_valid_group(mock_plt, sample_df):
    ax = task_func(sample_df, 'category', 'values', 'A')
    assert ax.xlabel_called_with == 'category'
    assert ax.ylabel_called_with == 'values'
    assert ax.title_called_with == 'Bar chart of values for A'
    assert ax.xticks_called_with == np.array([0, 1])
    assert ax.bar_called_with == (np.array([0, 1]), np.array([10, 30]), 0.35, ['r', 'g'])

def test_task_func_invalid_group(mock_plt, sample_df):
    with pytest.raises(ValueError):
        task_func(sample_df, 'category', 'values', 'D')

def test_task_func_single_group(mock_plt, sample_df):
    ax = task_func(sample_df, 'category', 'values', 'B')
    assert ax.xlabel_called_with == 'category'
    assert ax.ylabel_called_with == 'values'
    assert ax.title_called_with == 'Bar chart of values for B'
    assert ax.xticks_called_with == np.array([0])
    assert ax.bar_called_with == (np.array([0]), np.array([20]), 0.35, ['r'])
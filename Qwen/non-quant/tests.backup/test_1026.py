import pytest
from src_1026 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Mocking the plotting functionality
@pytest.fixture
def mock_plot(monkeypatch):
    def mock_show(*args, **kwargs):
        pass

    monkeypatch.setattr(plt, 'show', mock_show)

def test_task_func_empty_input(mock_plot):
    data_dict = {}
    df, ax = task_func(data_dict)
    assert df.empty
    assert ax.get_title() == "Scaled Values"

def test_task_func_no_missing_values(mock_plot):
    data_dict = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df, ax = task_func(data_dict)
    assert not df.empty
    assert ax.get_title() == "Scaled Values"
    assert df.shape == (3, 2)
    assert all(df.min() >= 0)
    assert all(df.max() <= 1)

def test_task_func_with_missing_values(mock_plot):
    data_dict = {'A': [1, None, 3], 'B': [4, 5, None]}
    df, ax = task_func(data_dict)
    assert not df.empty
    assert ax.get_title() == "Scaled Values"
    assert df.shape == (1, 2)
    assert all(df.min() >= 0)
    assert all(df.max() <= 1)

def test_task_func_single_value(mock_plot):
    data_dict = {'A': [1], 'B': [2]}
    df, ax = task_func(data_dict)
    assert not df.empty
    assert ax.get_title() == "Scaled Values"
    assert df.shape == (1, 2)
    assert all(df.min() == 0)
    assert all(df.max() == 0)

def test_task_func_negative_values(mock_plot):
    data_dict = {'A': [-1, -2, -3], 'B': [-4, -5, -6]}
    df, ax = task_func(data_dict)
    assert not df.empty
    assert ax.get_title() == "Scaled Values"
    assert df.shape == (3, 2)
    assert all(df.min() >= 0)
    assert all(df.max() <= 1)
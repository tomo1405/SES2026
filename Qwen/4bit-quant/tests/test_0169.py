import os

import matplotlib.pyplot as plt
import pandas as pd
from src_0169 import task_func


def test_task_func_default_labels():
    fig, data, plot_filename = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (5, 5)
    assert list(data.columns) == ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
    assert os.path.exists(plot_filename)
    os.remove(plot_filename)

def test_task_func_custom_labels():
    custom_labels = ['A', 'B', 'C', 'D', 'E']
    fig, data, plot_filename = task_func(labels=custom_labels)
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (5, 5)
    assert list(data.columns) == custom_labels
    assert os.path.exists(plot_filename)
    os.remove(plot_filename)

def test_task_func_different_data_size():
    fig, data, plot_filename = task_func(data_size=10)
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (10, 5)
    assert list(data.columns) == ['Group1', 'Group2', 'Group3', 'Group4', 'Group5']
    assert os.path.exists(plot_filename)
    os.remove(plot_filename)

def test_task_func_different_num_groups():
    fig, data, plot_filename = task_func(num_groups=3)
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (5, 3)
    assert list(data.columns) == ['Group1', 'Group2', 'Group3']
    assert os.path.exists(plot_filename)
    os.remove(plot_filename)

def test_task_func_custom_labels_and_data_size():
    custom_labels = ['X', 'Y', 'Z']
    fig, data, plot_filename = task_func(labels=custom_labels, data_size=7)
    assert isinstance(fig, plt.Figure)
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (7, 3)
    assert list(data.columns) == custom_labels
    assert os.path.exists(plot_filename)
    os.remove(plot_filename)
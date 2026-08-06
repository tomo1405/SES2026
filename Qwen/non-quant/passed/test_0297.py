import pytest
from src_0297 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_empty_dataframe():
    df = pd.DataFrame(columns=['value'])
    fig, ax = plt.subplots()
    assert task_func(df) == ax

def test_task_func_single_value():
    df = pd.DataFrame({'value': [1]})
    fig, ax = plt.subplots()
    assert task_func(df) == ax

def test_task_func_multiple_values():
    df = pd.DataFrame({'value': [1, 2, 2, 3, 3, 3]})
    fig, ax = plt.subplots()
    assert task_func(df) == ax

def test_task_func_plot_labels():
    df = pd.DataFrame({'value': [1, 2, 2, 3, 3, 3]})
    ax = task_func(df)
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Value Distribution'

def test_task_func_value_counts():
    df = pd.DataFrame({'value': [1, 2, 2, 3, 3, 3]})
    ax = task_func(df)
    bars = ax.patches
    expected_heights = [1, 2, 3]
    for bar, expected_height in zip(bars, expected_heights):
        assert bar.get_height() == expected_height
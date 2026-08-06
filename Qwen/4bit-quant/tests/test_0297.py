import pytest
from src_0297 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_input_type():
    with pytest.raises(ValueError):
        task_func([1, 2, 3])

def test_task_func_value_counts():
    df = pd.DataFrame({'value': [1, 2, 2, 3, 3, 3]})
    fig, ax = plt.subplots()
    task_func(df)
    assert len(ax.patches) == 3
    assert ax.patches[0].get_height() == 1
    assert ax.patches[1].get_height() == 2
    assert ax.patches[2].get_height() == 3

def test_task_func_labels_and_title():
    df = pd.DataFrame({'value': [1, 2, 2, 3, 3, 3]})
    fig, ax = plt.subplots()
    task_func(df)
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Count'
    assert ax.get_title() == 'Value Distribution'

def test_task_func_with_empty_df():
    df = pd.DataFrame({'value': []})
    fig, ax = plt.subplots()
    task_func(df)
    assert len(ax.patches) == 0
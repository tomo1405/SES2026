import pytest
from src_0166 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_default():
    fig = task_func()
    assert isinstance(fig, plt.Figure)
    data = pd.read_csv('output.csv')  # Assuming the plot is saved to a CSV file for verification
    assert len(data) == 5
    assert all(col in data.columns for col in ['A', 'B', 'C', 'D', 'E'])

def test_task_func_custom_rows_and_range():
    num_rows = 10
    rand_range = (50, 200)
    fig = task_func(num_rows=num_rows, rand_range=rand_range)
    assert isinstance(fig, plt.Figure)
    data = pd.read_csv('output.csv')  # Assuming the plot is saved to a CSV file for verification
    assert len(data) == num_rows
    assert all(col in data.columns for col in ['A', 'B', 'C', 'D', 'E'])
    assert all(data[col].between(rand_range[0], rand_range[1]).all() for col in data.columns)
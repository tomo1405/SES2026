import matplotlib.pyplot as plt
import pandas as pd
from src_0168 import task_func


def test_task_func_return_type():
    fig, ax = task_func()
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)

def test_task_func_dataframe_shape():
    num_types = 5
    fig, ax = task_func(num_types=num_types)
    data = pd.DataFrame({label: [randint(*integer_range) for _ in range(num_types)] for label in [f'Type{i + 1}' for i in range(num_types)]})
    assert data.shape == (num_types, num_types)

def test_task_func_labels():
    num_types = 5
    fig, ax = task_func(num_types=num_types)
    labels = [f'Type{i + 1}' for i in range(num_types)]
    for label in labels:
        assert label in ax.get_legend().get_texts()

def test_task_func_integer_range():
    integer_range = (0, 100)
    fig, ax = task_func(integer_range=integer_range)
    data = pd.DataFrame({label: [randint(*integer_range) for _ in range(5)] for label in [f'Type{i + 1}' for i in range(5)]})
    assert all(0 <= value <= 100 for value in data.values.flatten())

def test_task_func_plot_type():
    fig, ax = task_func()
    assert ax.get_xlabel() == 'Type'
    assert ax.get_ylabel() == 'Value'
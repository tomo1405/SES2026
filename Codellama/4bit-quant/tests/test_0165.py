import matplotlib
import numpy as np
import pandas as pd
from src_0165 import task_func


def test_task_func():
    # Test that the function returns a figure object
    fig = task_func()
    assert isinstance(fig, matplotlib.figure.Figure)

    # Test that the function creates a bar plot with the correct number of bars
    num_labels = 5
    data = pd.DataFrame(np.random.uniform(0, 1, size=(num_labels, num_labels)), columns=['Label1', 'Label2', 'Label3', 'Label4', 'Label5'])
    fig = task_func(num_labels=num_labels, data_range=(0, 1))
    assert len(fig.axes[0].patches) == num_labels

    # Test that the function creates a bar plot with the correct bar heights
    data = pd.DataFrame(np.random.uniform(0, 1, size=(num_labels, num_labels)), columns=['Label1', 'Label2', 'Label3', 'Label4', 'Label5'])
    fig = task_func(num_labels=num_labels, data_range=(0, 1))
    assert np.allclose(fig.axes[0].patches[0].get_height(), data.iloc[0, 0])
    assert np.allclose(fig.axes[0].patches[1].get_height(), data.iloc[0, 1])
    assert np.allclose(fig.axes[0].patches[2].get_height(), data.iloc[0, 2])
    assert np.allclose(fig.axes[0].patches[3].get_height(), data.iloc[0, 3])
    assert np.allclose(fig.axes[0].patches[4].get_height(), data.iloc[0, 4])

    # Test that the function creates a bar plot with the correct bar positions
    data = pd.DataFrame(np.random.uniform(0, 1, size=(num_labels, num_labels)), columns=['Label1', 'Label2', 'Label3', 'Label4', 'Label5'])
    fig = task_func(num_labels=num_labels, data_range=(0, 1))
    assert np.allclose(fig.axes[0].patches[0].get_x(), data.columns[0])
    assert np.allclose(fig.axes[0].patches[1].get_x(), data.columns[1])
    assert np.allclose(fig.axes[0].patches[2].get_x(), data.columns[2])
    assert np.allclose(fig.axes[0].patches[3].get_x(), data.columns[3])
    assert np.allclose(fig.axes[0].patches[4].get_x(), data.columns[4])

    # Test that the function creates a bar plot with the correct bar widths
    data = pd.DataFrame(np.random.uniform(0, 1, size=(num_labels, num_labels)), columns=['Label1', 'Label2', 'Label3', 'Label4', 'Label5'])
    fig = task_func(num_labels=num_labels, data_range=(0, 1))
    assert np.allclose(fig.axes[0].patches[0].get_width(), 1)
    assert np.allclose(fig.axes[0].patches[1].get_width(), 1)
    assert np.allclose(fig.axes[0].patches[2].get_width(), 1)
    assert np.allclose(fig.axes[0].patches[3].get_width(), 1)
    assert np.allclose(fig.axes[0].patches[4].get_width(), 1)

    # Test that the function creates a bar plot with the correct bar colors
    data = pd.DataFrame(np.random.uniform(0, 1, size=(num_labels, num_labels)), columns=['Label1', 'Label2', 'Label3', 'Label4', 'Label5'])
    fig = task_func(num_labels=num_labels, data_range=(0, 1))
    assert np.allclose(fig.axes[0].patches[0].get_facecolor(), 'blue')
    assert np.allclose(fig.axes[0].patches[1].get_facecolor(), 'red')
    assert np.allclose(fig.axes[0].patches[2].get_facecolor(), 'green')
    assert np.allclose(fig.axes[0].patches[3].get_facecolor(), 'yellow')
    assert np.allclose(fig.axes[0].patches[4].get_facecolor(), 'black')
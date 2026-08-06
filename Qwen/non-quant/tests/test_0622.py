import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from src_0622 import task_func


def test_task_func_output_type():
    L = [[1, 2], [3, 4]]
    ax = task_func(L)
    assert isinstance(ax, plt.Axes)

def test_task_func_data_standardization():
    L = [[1, 2], [3, 4]]
    ax = task_func(L)
    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)
    
    scaler = StandardScaler()
    expected_data = scaler.fit_transform(data)
    
    # Extract the data from the plot
    lines = ax.get_lines()
    plotted_data = lines[0].get_ydata()
    
    assert np.allclose(plotted_data, expected_data.flatten())

def test_task_func_plot_closed():
    L = [[1, 2], [3, 4]]
    ax = task_func(L)
    fig = ax.get_figure()
    assert fig.canvas.manager.window is None  # Check if the figure is closed

def test_task_func_empty_input():
    L = []
    ax = task_func(L)
    data = list(chain(*L))
    data = np.array(data).reshape(-1, 1)
    
    scaler = StandardScaler()
    expected_data = scaler.fit_transform(data)
    
    # Extract the data from the plot
    lines = ax.get_lines()
    plotted_data = lines[0].get_ydata()
    
    assert np.allclose(plotted_data, expected_data.flatten())
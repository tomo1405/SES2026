import pytest
from src_0660 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Sample data
    x = [np.linspace(-3, 3, 100) for _ in range(2)]
    y = [
        np.random.normal(loc=0, scale=1, size=100),
        np.random.normal(loc=1, scale=2, size=100)
    ]
    labels = ['Distribution 1', 'Distribution 2']

    # Call the function
    fig = task_func(x, y, labels)

    # Check if the returned object is a matplotlib figure
    assert isinstance(fig, plt.Figure)

    # Check if the figure has at least one axis
    assert len(fig.axes) > 0

    # Check if the legend has the correct number of entries
    legend = fig.axes[0].get_legend()
    assert legend is not None
    assert len(legend.get_lines()) == len(labels)

    # Check if the plot has the correct number of lines
    lines = fig.axes[0].lines
    assert len(lines) == len(labels)

    # Clean up the plot to avoid interference with other tests
    plt.close(fig)
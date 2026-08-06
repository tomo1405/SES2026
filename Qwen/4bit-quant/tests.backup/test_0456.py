import pytest
from src_0456 import task_func
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import io

# Mocking matplotlib to capture plot output
class MockPlot:
    def __init__(self):
        self.figures = []

    def figure(self, *args, **kwargs):
        fig = plt.Figure(*args, **kwargs)
        self.figures.append(fig)
        return fig

    def show(self):
        pass

@pytest.fixture(autouse=True)
def mock_plot(monkeypatch):
    mp = MockPlot()
    monkeypatch.setattr(plt, 'figure', mp.figure)
    monkeypatch.setattr(plt, 'show', mp.show)
    return mp

def test_task_func(mock_plot):
    mean = 0
    std_dev = 1
    n = 1000
    samples = task_func(mean, std_dev, n)

    # Check if the number of samples is correct
    assert len(samples) == n

    # Check if the samples are approximately normally distributed
    _, p_value = stats.kstest(samples, 'norm', args=(mean, std_dev))
    assert p_value > 0.05, "The samples do not appear to be normally distributed."

    # Check if a plot was created
    assert len(mock_plot.figures) == 1, "No plot was created."

    # Check if the plot has the correct title
    fig = mock_plot.figures[0]
    assert fig.axes[0].get_title() == f'Normal Distribution: Mean = {mean}, Std Dev = {std_dev}'

    # Check if the plot has the correct labels
    assert fig.axes[0].get_xlabel() == 'Value'
    assert fig.axes[0].get_ylabel() == 'Density'
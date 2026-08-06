import pytest
from src_0254 import task_func
import matplotlib.pyplot as plt

@pytest.fixture
def ax():
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    return ax

def test_task_func_returns_color(ax):
    color = task_func(ax)
    assert color in task_func.COLORS

def test_task_func_plots_line(ax, mocker):
    mock_plot = mocker.patch('matplotlib.axes.Axes.plot')
    task_func(ax)
    mock_plot.assert_called_once()

def test_task_func_sets_rlabel_position(ax, mocker):
    mock_set_rlabel_position = mocker.patch('matplotlib.axes.Axes.set_rlabel_position')
    task_func(ax)
    mock_set_rlabel_position.assert_called_once()
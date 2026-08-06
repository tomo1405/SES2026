import matplotlib.pyplot as plt
import pytest
from src_0256 import task_func

@pytest.fixture
def ax():
    return plt.subplot(111)

def test_ax_type(ax):
    assert isinstance(task_func(ax, 0), matplotlib.axes.Axes)

def test_ax_value_error(ax):
    with pytest.raises(ValueError):
        task_func("not_an_axes", 0)

def test_plot_data(ax):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(x)
    ax = task_func(ax, 0)
    assert np.array_equal(ax.lines[0].get_xdata(), x)
    assert np.array_equal(ax.lines[0].get_ydata(), y)

def test_rlabel_position(ax):
    rlabel_positions = [45, 90, 135]
    for i in range(3):
        ax = task_func(ax, i)
        assert ax.get_rlabel_position() == rlabel_positions[i]
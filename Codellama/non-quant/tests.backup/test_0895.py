import pytest
from src_0895 import task_func

def test_task_func():
    array, mean, std, ax = task_func()
    assert isinstance(array, np.ndarray)
    assert array.shape == (ARRAY_SIZE,)
    assert np.all(array >= 1) and np.all(array <= 100)
    assert np.isclose(mean, np.mean(array))
    assert np.isclose(std, np.std(array))
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Histogram of Random Integers'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_legend() == ["Mean", "Standard Deviation"]
    assert len(ax.get_lines()) == 3
    assert ax.get_lines()[0].get_color() == 'red'
    assert ax.get_lines()[0].get_linestyle() == 'dashed'
    assert ax.get_lines()[0].get_linewidth() == 1
    assert ax.get_lines()[1].get_color() == 'purple'
    assert ax.get_lines()[1].get_linestyle() == 'dashed'
    assert ax.get_lines()[1].get_linewidth() == 1
    assert ax.get_lines()[2].get_color() == 'purple'
    assert ax.get_lines()[2].get_linestyle() == 'dashed'
    assert ax.get_lines()[2].get_linewidth() == 1
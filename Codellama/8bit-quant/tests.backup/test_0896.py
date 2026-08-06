import pytest
from src_0896 import task_func

def test_task_func():
    array, mean, std, ax = task_func()
    assert isinstance(array, np.ndarray)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(array) == ARRAY_SIZE
    assert np.mean(array) == pytest.approx(mean)
    assert np.std(array) == pytest.approx(std)
    assert ax.get_title() == 'Histogram of Random Values'
    assert ax.get_xlabel() == 'Val'
    assert ax.get_ylabel() == 'Freq'
    assert ax.get_xlim() == (1, 500)
    assert ax.get_ylim() == (0, 10000)
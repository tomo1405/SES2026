import numpy as np
from src_0896 import task_func


def test_task_func():
    array, mean, std, ax = task_func()
    assert isinstance(array, np.ndarray)
    assert array.shape == (ARRAY_SIZE,)
    assert np.all(array >= 1) and np.all(array <= 500)
    assert np.isclose(mean, np.mean(array))
    assert np.isclose(std, np.std(array))
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Histogram of Random Values'
    assert ax.get_xlabel() == 'Val'
    assert ax.get_ylabel() == 'Freq'
    assert ax.get_xlim() == (1, 500)
    assert ax.get_ylim() == (0, 10000)
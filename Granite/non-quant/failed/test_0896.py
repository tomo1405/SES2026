import pytest
from src_0896 import task_func

def test_task_func():
    array, mean, std, ax = task_func()
    assert isinstance(array, np.ndarray)
    assert isinstance(mean, float)
    assert isinstance(std, float)
    assert isinstance(ax, plt.Axes)
    assert array.shape == (ARRAY_SIZE,)
    assert mean > 0 and mean < 500
    assert std > 0 and std < 500
    assert ax.get_title() == 'Histogram of Random Values'
    assert ax.get_xlabel() == 'Val'
    assert ax.get_ylabel() == 'Freq'
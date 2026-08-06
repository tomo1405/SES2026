import pytest
from src_0357 import task_func

def test_task_func():
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    ax, Z = task_func(x, y)
    assert ax is not None
    assert Z.shape == (len(y), len(x))
    assert np.amin(Z) >= 0
    assert np.amax(Z) <= 2 * np.pi

def test_task_func_empty_arrays():
    x = np.array([])
    y = np.array([])
    ax, Z = task_func(x, y)
    assert ax is None
    assert Z.size == 0

def test_task_func_mismatched_arrays():
    x = np.array([1, 2, 3])
    y = np.array([4, 5])
    with pytest.raises(ValueError):
        task_func(x, y)
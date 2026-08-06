import pytest
from src_0238 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func_basic():
    data = [
        ('item1', 1, 2, 3),
        ('item2', 4, 5, 6),
        ('item3', 7, 8, 9)
    ]
    result = task_func(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 2)

def test_task_func_save_plot_without_path():
    data = [
        ('item1', 1, 2, 3),
        ('item2', 4, 5, 6),
        ('item3', 7, 8, 9)
    ]
    with pytest.raises(ValueError):
        task_func(data, save_plot=True)

def test_task_func_save_plot_with_path(tmpdir):
    data = [
        ('item1', 1, 2, 3),
        ('item2', 4, 5, 6),
        ('item3', 7, 8, 9)
    ]
    plot_path = str(tmpdir / "test_plot.png")
    result, ax = task_func(data, save_plot=True, plot_path=plot_path)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 2)
    assert ax is not None
    assert plt.fignum_exists(1) is False  # Plot should be closed after saving

def test_task_func_no_save_plot():
    data = [
        ('item1', 1, 2, 3),
        ('item2', 4, 5, 6),
        ('item3', 7, 8, 9)
    ]
    result = task_func(data, save_plot=False)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 2)
    assert plt.fignum_exists(1) is True  # Plot should still be open

def test_task_func_empty_data():
    data = []
    result = task_func(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (0, 2)

def test_task_func_single_item():
    data = [('item1', 1, 2, 3)]
    result = task_func(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (1, 2)
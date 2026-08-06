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

def test_task_func_save_plot():
    data = [
        ('item1', 1, 2, 3),
        ('item2', 4, 5, 6),
        ('item3', 7, 8, 9)
    ]
    with pytest.raises(ValueError):
        task_func(data, save_plot=True)

    with pytest.raises(FileNotFoundError):
        task_func(data, save_plot=True, plot_path='non_existent_directory/test.png')

    # Assuming 'test.png' is a writable path in your environment
    result = task_func(data, save_plot=True, plot_path='test.png')
    assert isinstance(result, tuple)
    coordinates_2d, ax = result
    assert isinstance(coordinates_2d, np.ndarray)
    assert coordinates_2d.shape == (3, 2)
    assert isinstance(ax, plt.Axes)

def test_task_func_no_plot():
    data = []
    result = task_func(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (0, 2)

def test_task_func_single_item():
    data = [('item1', 1, 2, 3)]
    result = task_func(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (1, 2)

def test_task_func_duplicate_items():
    data = [
        ('item1', 1, 2, 3),
        ('item1', 1, 2, 3),
        ('item2', 4, 5, 6)
    ]
    result = task_func(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 2)
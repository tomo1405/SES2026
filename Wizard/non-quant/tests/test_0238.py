python
import numpy as np
import pytest
from src_0238 import task_func

def test_task_func():
    # Test case 1: Test with default values
    data = [("item1", 1, 2, 3), ("item2", 4, 5, 6), ("item3", 7, 8, 9)]
    expected_coordinates_2d = [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0)]
    expected_ax = None
    coordinates_2d, ax = task_func(data)
    assert np.allclose(coordinates_2d, expected_coordinates_2d)
    assert ax == expected_ax

    # Test case 2: Test with save_plot=True and plot_path=None
    data = [("item1", 1, 2, 3), ("item2", 4, 5, 6), ("item3", 7, 8, 9)]
    expected_coordinates_2d = [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0)]
    expected_ax = None
    with pytest.raises(ValueError):
        coordinates_2d, ax = task_func(data, save_plot=True)

    # Test case 3: Test with save_plot=True and plot_path="test.png"
    data = [("item1", 1, 2, 3), ("item2", 4, 5, 6), ("item3", 7, 8, 9)]
    expected_coordinates_2d = [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0)]
    expected_ax = None
    coordinates_2d, ax = task_func(data, save_plot=True, plot_path="test.png")
    assert np.allclose(coordinates_2d, expected_coordinates_2d)
    assert ax == expected_ax
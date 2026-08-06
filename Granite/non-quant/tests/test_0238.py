import pytest
from src_0238 import task_func

def test_task_func():
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    coordinates_2d, ax = task_func(data, save_plot=False, plot_path=None)
    assert isinstance(coordinates_2d, np.ndarray)
    assert ax is not None
    assert ax.get_xlabel() == 'component 1'
    assert ax.get_ylabel() == 'component 2'

def test_task_func_with_save_plot():
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    plot_path = 'test_plot.png'
    coordinates_2d, ax = task_func(data, save_plot=True, plot_path=plot_path)
    assert isinstance(coordinates_2d, np.ndarray)
    assert ax is not None
    assert ax.get_xlabel() == 'component 1'
    assert ax.get_ylabel() == 'component 2'
    assert os.path.exists(plot_path)
    os.remove(plot_path)
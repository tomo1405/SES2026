import pytest
from src_1054 import task_func


def test_task_func_valid_file():
    file_path = "test_data.csv"
    save_path = "test_plot.png"
    ax = task_func(file_path, save_path)
    assert ax is not None
    assert isinstance(ax, matplotlib.axes.Axes)
    assert os.path.exists(save_path)


def test_task_func_invalid_file():
    file_path = "invalid_file.csv"
    save_path = "test_plot.png"
    with pytest.raises(FileNotFoundError):
        task_func(file_path, save_path)


def test_task_func_no_save_path():
    file_path = "test_data.csv"
    ax = task_func(file_path)
    assert ax is not None
    assert isinstance(ax, matplotlib.axes.Axes)
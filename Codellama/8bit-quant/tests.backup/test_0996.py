import pytest
from src_0996 import task_func

def test_task_func_file_not_found():
    file_path = "path/to/file.csv"
    plot_path = "path/to/plot.png"
    with pytest.raises(FileNotFoundError):
        task_func(file_path, plot_path)

def test_task_func_empty_file():
    file_path = "path/to/empty_file.csv"
    plot_path = "path/to/plot.png"
    mean, median, plot_path = task_func(file_path, plot_path)
    assert mean == np.nan
    assert median == np.nan
    assert plot_path == "path/to/plot.png"

def test_task_func_valid_file():
    file_path = "path/to/valid_file.csv"
    plot_path = "path/to/plot.png"
    mean, median, plot_path = task_func(file_path, plot_path)
    assert mean == 10.0
    assert median == 10.0
    assert plot_path == "path/to/plot.png"
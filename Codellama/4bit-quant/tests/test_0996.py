import pytest
from src_0996 import task_func

def test_task_func_valid_file():
    file_path = "path/to/valid/file.csv"
    plot_path = "path/to/plot.png"
    mean, median, plot_path = task_func(file_path, plot_path)
    assert mean == 10.0
    assert median == 10.0
    assert plot_path == "path/to/plot.png"

def test_task_func_invalid_file():
    file_path = "path/to/invalid/file.csv"
    plot_path = "path/to/plot.png"
    with pytest.raises(FileNotFoundError):
        task_func(file_path, plot_path)

def test_task_func_empty_file():
    file_path = "path/to/empty/file.csv"
    plot_path = "path/to/plot.png"
    mean, median, plot_path = task_func(file_path, plot_path)
    assert mean == np.nan
    assert median == np.nan
    assert plot_path == "path/to/plot.png"

def test_task_func_invalid_data():
    file_path = "path/to/invalid/data.csv"
    plot_path = "path/to/plot.png"
    mean, median, plot_path = task_func(file_path, plot_path)
    assert mean == np.nan
    assert median == np.nan
    assert plot_path == "path/to/plot.png"
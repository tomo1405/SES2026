import pytest
from src_1055 import task_func

def test_task_func():
    file_path = "path/to/file.csv"
    mean, std_dev, ax = task_func(file_path)
    assert isinstance(mean, float)
    assert isinstance(std_dev, float)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == "Sample Values"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Sample Histogram with Normal Distribution Overlay"
    assert len(ax.get_lines()) == 1
    assert ax.get_lines()[0].get_color() == "k"
    assert ax.get_lines()[0].get_linewidth() == 2

def test_task_func_invalid_file():
    file_path = "path/to/invalid_file.csv"
    with pytest.raises(IOError):
        task_func(file_path)
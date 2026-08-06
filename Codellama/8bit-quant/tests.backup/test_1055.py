import pytest
from src_1055 import task_func

def test_task_func():
    file_path = "test_data.csv"
    mean, std_dev, ax = task_func(file_path)
    assert isinstance(mean, float)
    assert isinstance(std_dev, float)
    assert isinstance(ax, matplotlib.axes.Axes)

    with pytest.raises(IOError):
        task_func("invalid_file_path")
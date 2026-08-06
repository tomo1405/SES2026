import pytest
from src_1055 import task_func

def test_task_func():
    file_path = "path/to/file.csv"
    mean, std_dev, ax = task_func(file_path)
    assert isinstance(mean, float), "Mean should be a float"
    assert isinstance(std_dev, float), "Standard deviation should be a float"
    assert isinstance(ax, object), "Ax should be an object"
    assert mean >= 0, "Mean should be non-negative"
    assert std_dev >= 0, "Standard deviation should be non-negative"

def test_task_func_ioerror():
    file_path = "path/to/invalid_file.csv"
    with pytest.raises(IOError) as exc_info:
        task_func(file_path)
    assert "Error reading the file" in str(exc_info.value), "IOError should be raised with specific message"
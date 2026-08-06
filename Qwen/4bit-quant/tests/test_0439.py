import pytest
from src_0439 import task_func
import os
import matplotlib.pyplot as plt

def test_task_func_with_valid_input():
    numbers = [1, 2, 3, 4, 5]
    result = task_func(numbers)
    assert isinstance(result, plt.Figure)
    assert len(result.axes) == 1
    assert len(result.axes[0].lines) == 1
    assert result.axes[0].lines[0].get_data() == ([0, 1, 2, 3, 4], [1, 2, 3, 4, 5])

def test_task_func_with_invalid_input_type():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_with_invalid_list_elements():
    with pytest.raises(TypeError):
        task_func([1, "two", 3])

def test_task_func_with_file_path():
    numbers = [1, 2, 3]
    file_path = "test_save.pkl"
    result = task_func(numbers, file_path)
    assert isinstance(result, plt.Figure)
    assert os.path.exists(file_path) is False  # File should be deleted after loading

def test_task_func_with_default_file_path():
    numbers = [1, 2, 3]
    result = task_func(numbers)
    assert isinstance(result, plt.Figure)
    assert os.path.exists("save.pkl") is False  # Default file should be deleted after loading
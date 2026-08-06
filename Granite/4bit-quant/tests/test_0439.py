import pickle
import os
import matplotlib.pyplot as plt
from src_0439 import task_func
import pytest

def test_task_func_valid_input():
    numbers = [1, 2, 3, 4, 5]
    loaded_fig = task_func(numbers)
    assert isinstance(loaded_fig, plt.Figure)

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_file_path():
    numbers = [1, 2, 3, 4, 5]
    file_path = "test_save.pkl"
    loaded_fig = task_func(numbers, file_path)
    assert loaded_fig is not None
    os.remove(file_path)
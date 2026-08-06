import pytest
from src_0439 import task_func
import pickle
import os
import matplotlib.pyplot as plt

def test_task_func_valid_input():
    numbers = [1, 2, 3, 4, 5]
    result = task_func(numbers)
    assert isinstance(result, plt.figure.Figure)

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_file_operations():
    numbers = [1, 2, 3, 4, 5]
    result = task_func(numbers)
    assert os.path.exists("save.pkl")
    os.remove("save.pkl")
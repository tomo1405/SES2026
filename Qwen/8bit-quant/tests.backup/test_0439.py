import pytest
from src_0439 import task_func
import os
import pickle
import matplotlib.pyplot as plt

def test_task_func_with_valid_input():
    numbers = [1, 2, 3, 4, 5]
    result = task_func(numbers)
    assert isinstance(result, plt.Figure)

def test_task_func_with_invalid_input_type():
    numbers = "not a list"
    with pytest.raises(TypeError):
        task_func(numbers)

def test_task_func_with_invalid_list_contents():
    numbers = [1, "two", 3, 4.5]
    with pytest.raises(TypeError):
        task_func(numbers)

def test_task_func_with_custom_file_path():
    numbers = [1, 2, 3, 4, 5]
    file_path = "custom_save.pkl"
    result = task_func(numbers, file_path=file_path)
    assert isinstance(result, plt.Figure)
    assert not os.path.exists(file_path)  # Ensure the file is removed after use

def test_task_func_with_no_file_path_provided():
    numbers = [1, 2, 3, 4, 5]
    result = task_func(numbers)
    assert isinstance(result, plt.Figure)

def test_task_func_with_empty_list():
    numbers = []
    result = task_func(numbers)
    assert isinstance(result, plt.Figure)

def test_task_func_with_single_element_list():
    numbers = [42]
    result = task_func(numbers)
    assert isinstance(result, plt.Figure)